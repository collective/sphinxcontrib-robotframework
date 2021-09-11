# -*- coding: utf-8 -*-
from docutils.parsers.rst import Directive
import docutils
import hashlib
import os
import pickle
import robot
import tempfile

from sphinx.directives import CodeBlock
from sphinx.errors import SphinxError

ROBOT_PICKLE_FILENAME = 'robotframework.pickle'


class RobotAwareCodeBlock(CodeBlock):

    option_spec = dict(
        list(docutils.parsers.rst.directives.body.CodeBlock.option_spec.items())
        + list(CodeBlock.option_spec.items())
    )

    def run(self):
        app = self.state_machine.document.settings.env.app
        document = self.state_machine.document

        if 'robotframework' in self.arguments:
            robot_source = u'\n'.join(self.content)
            if not hasattr(document, '_robot_source'):
                document._robot_source = robot_source
            else:
                document._robot_source += u'\n' + robot_source

            if 'hidden' in (self.options.get('class', []) or []):
                return []  # suppress nodes with :class: hidden
            if app.config.sphinxcontrib_robotframework_quiet:
                return []  # suppress nodes when required in settings

        return super(RobotAwareCodeBlock, self).run()


def creates_option(argument):
    """Splitslist of filenames into a list (and defaults to an empty list).
    """
    return filter(bool, argument.split() if argument else [])


class RobotSettingsDirective(Directive):
    """Per-document directive for controlling Robot Framework tests
    """
    has_content = False
    option_spec = {
        'creates': creates_option,
    }

    def run(self):
        # This directive was made obsolete in >= 0.5.0 and is now waiting for a
        # new purpose...
        return []


def get_robot_variables():
    """Return list of Robot Framework -compatible cli-variables parsed
    from ROBOT_-prefixed environment variable

    """
    prefix = 'ROBOT_'
    variables = []
    for key in os.environ:
        if key.startswith(prefix) and len(key) > len(prefix):
            variables.append('%s:%s' % (key[len(prefix):], os.environ[key]))
    return variables


def run_robot(app, doctree, docname):
    # Tests can be switched off with a global setting:
    if not app.config.sphinxcontrib_robotframework_enabled:
        return

    # Set up a variable for 'the current working directory':
    robot_dir = os.path.dirname(os.path.join(app.srcdir, docname))

    # Tests are only run when they are found:
    if not hasattr(doctree, '_robot_source'):
        return

    # Skip already run robotframework suites
    checksums_filename = os.path.join(app.doctreedir, ROBOT_PICKLE_FILENAME)
    try:
        with open(checksums_filename, 'rb') as fp:
            checksums = pickle.loads(fp.read())
    except (IOError, EOFError, TypeError, IndexError):
        checksums = []
    checksum = hashlib.md5(doctree._robot_source.encode('utf-8')).hexdigest()
    if checksum in checksums:
        return

    # Build a test suite:
    robot_file = tempfile.NamedTemporaryFile(dir=robot_dir, suffix='.robot')
    robot_file.write(doctree._robot_source.encode('utf-8'))
    robot_file.flush()  # flush buffer into file

    # Skip running when the source has no test cases (e.g. has settings)
    try:
        robot_suite = robot.running.TestSuiteBuilder().build(robot_file.name)
    except robot.errors.DataError as e:
        if e.message.endswith('File has no test case table.'):
            return
        raise
    except AttributeError as e:
        # Fix to make this package still work with robotframework < 2.8.x
        pass
    if not len(robot_suite.tests):
        return

    # Get robot variables from environment
    env_robot_variables = get_robot_variables()
    env_robot_keys = [var.split(':')[0] for var in env_robot_variables]

    # Run the test suite:
    output = os.path.join(
        robot_dir, '{0:s}.output.xml'.format(robot_file.name))
    log = os.path.join(
        robot_dir, '{0:s}.log.html'.format(robot_file.name))
    options = {
        'outputdir': robot_dir,
        'output': output,
        'log': log,
        'report': 'NONE',
        'variable': env_robot_variables + [
            '%s:%s' % (key, value) for key, value
            in app.config.sphinxcontrib_robotframework_variables.items()
            if not key in env_robot_keys
        ]
    }

    # Update persisted checksums
    nitpicky = getattr(app.config, 'nitpicky', False)
    result = robot.run(robot_file.name, **options)
    if result == 0:
        with open(checksums_filename, 'wb') as fp:
            fp.write(pickle.dumps(checksums + [checksum]))
    elif nitpicky:
        raise SphinxError('Robot Framework reported errors. '
                          'Please, see "{0:s}" for details.'.format(log))
    if os.path.isfile(output):
        os.unlink(output)
    if os.path.isfile(log):
        os.unlink(log)

    # Close the test suite (and delete it, because it's a tempfile):
    robot_file.close()

    # Re-process images to include robot generated images:
    if os.path.sep in docname:
        # Because process_images is not designed to be called more than once,
        # calling it with docnames with sub-directories needs a bit cleanup:
        removable = os.path.dirname(docname) + os.path.sep
        for node in doctree.traverse(docutils.nodes.image):
            if node['uri'].startswith(removable):
                node['uri'] = node['uri'][len(removable):]
    try:
        app.env.process_images(docname, doctree)
    except AttributeError:  # Sphinx >= 1.5
        app.env.temp_data['docname'] = docname
        from sphinx.environment.collectors.asset import ImageCollector
        ImageCollector().process_doc(app, doctree)
        del app.env.temp_data['docname']


def setup(app):
    app.add_config_value('sphinxcontrib_robotframework_enabled', True, True)
    app.add_config_value('sphinxcontrib_robotframework_variables', {}, True)
    app.add_config_value('sphinxcontrib_robotframework_quiet', False, True)
    app.add_directive('code', RobotAwareCodeBlock)
    app.add_directive('robotframework', RobotSettingsDirective)
    app.connect('doctree-resolved', run_robot)
