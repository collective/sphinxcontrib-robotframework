Robot Framework extension for Sphinx
====================================

**sphinxcontrib-robotframework** is a Sphinx_-extension, which executes embedded `Robot Framework`_ tests during ``sphinx-build``.

**sphinxcontrib-robotframework** can be used in doctest_ way to validate examples shown in documentation or with Selenium_ and its Robot Framework integration, Selenium2Library_, to generate scripted screenshots during the documentation compiliation time, for CI-generated up-to-date screenshots.

.. _Robot Framework: http://robotframework.org/
.. _Selenium2Library: https://github.com/rtomac/robotframework-selenium2library
.. _Selenium: http://docs.seleniumhq.org/
.. _Sphinx: http://sphinx-doc.org/
.. _doctest: https://docs.python.org/2/library/doctest.html


Examples
--------

.. toctree::
   :maxdepth: 2

   example
   screenshot
   annotations/example


Getting started
---------------

1. Install **sphinxcontrib-robotframework** into your virtualenv or require it as a dependency of your Sphinx-project.

2. Enable the extension and execution of embedded Robot Framework tests by adding the following lines into your Sphinx-project's ``conf.py``:

   .. code:: python

      extensions = ['sphinxcontrib_robotframework']

      # Enable Robot Framework tests during Sphinx compilation
      sphinxcontrib_robotframework_enabled = True

      # Hide Robot Framework syntax from the Sphinx output by default
      # (preferred, when you use the extension for scripted screenshots)
      sphinxcontrib_robotframework_quiet = True

3. Write your Robot Framework tests in space separated form as contents of Docutils' ``code``-directives with ``robotframework``-language:

   .. code:: restructuredtext

       .. code:: robotframework

          *** Settings ***

          ...

          *** Variables ***

          ...

          *** Test cases ***

          ...

   Each document may contain several ``code``-directives, but their contents are concatenated into a single Robot Framework test suite before execution.

   The output of each ``code``-directive can be omitted by setting a special ``:class: hidden``-option. (This is not a standard Sphinx-behavior, but a hard coded feature in **sphinxcontrib-robotframework**.)

4. Compile your documentation and see your tests being run.

.. note::

   If you choose to use Robot Framework variables in your test cases, you can override values for those variables in your Sphinx-configuration file (``conf.py``) with:

   .. code:: python

      sphinxcontrib_robotframework_variables = {
          "VARIABLE": "value"
      }
