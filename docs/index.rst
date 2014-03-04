Sphinx-extension for Robot Framework
====================================

`sphinxcontrib-robotframework`_ is a Sphinx-extensions, which executes
embedded `Robot Framework`_-tests during Sphinx-documentation compilation.

Usage
-----

1. Install `sphinxcontrib-robotframework`_ into your virtualenv or
   require it as a dependency of your project.

2. Enable the extension and automatic test runs by adding the following lines
   into your Sphinx-project's ``conf.py``:

   .. code:: python

      extensions = ['sphinxcontrib_robotframework']

      # Enable Robot Framework tests during Sphinx compilation
      sphinxcontrib_robotframework_enabled = True

      # Hide Robot Framework syntax form the Sphinx output by default
      sphinxcontrib_robotframework_quiet = True

3. Write your Robot Framework tests in space separated form as contents of
   Docutils' ``code``-directives with ``robotframework``-language, e.g.:

   .. code:: restructuredtext

       .. code:: robotframework

          *** Settings ***

          ...

          *** Variables ***

          ...

          *** Test cases ***

          ...

   Each document may contain several ``code``-directives, but be aware that
   their contents are concatenated into a single Robot Framework test suite
   before execution.

4. Compile your documentation and see your tests being run.

.. note::

   If you choose to use Robot Framework variables in your test cases,
   you can override values for those variables in your Sphinx-configuration
   file (``conf.py``) with:

   .. code:: python

      sphinxcontrib_robotframework_variables = {
          "VARIABLE": "value"
      }

Examples
--------

.. toctree::
   :maxdepth: 2

   example
   screenshot
   annotations/example

.. Links:
.. _sphinxcontrib-robotframework:
   http://pypi.python.org/pypi/sphinxcontrib-robotframework
.. _Robot Framework: http://robotframework.org/
