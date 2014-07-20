# -*- coding: utf-8 -*-
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinxcontrib_robotframework",
]

# Enable Robot Framework tests during Sphinx compilation.
sphinxcontrib_robotframework_enabled = True

# Hide Robot Framework syntax from the Sphinx output by default
# (preferred, when you use the extension for scripted screenshots)
sphinxcontrib_robotframework_quiet = False

# Configure Robot Frameowrk tests to use Firefox
sphinxcontrib_robotframework_variables = {
    "BROWSER": "Firefox"
}

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'sphinxcontrib-robotframework'
copyright = u'vivek <1990vivekkumarverma@gmail.com>, '\
            u'Asko Soukka <asko.soukka@iki.fi>'

# General information about the project.

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.4'
# The full version, including alpha/beta/rc tags.
release = '0.4.3'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'pyramid'

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinxcontrib-robotframework'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
}

latex_documents = [
    # (source target file, target latex name, document title,
    #  author, document clas [howto/manual]),
    ('index', 'sphinxcontrib-robotframework.tex',
     u'Robot Framework Sphinx Contrib Library Documentation',
     u'asko.soukka@iki.fi', 'manual'),
]
