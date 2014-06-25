Document with a screenshot
==========================

The fun with `sphinxcontrib-robotframework`_ starts in using it with
`robotframework-selenium2library`_. Together, they allow you to navigate any
website, take screenshots when required and finally embed those screenshot into
this very Sphinx-documentation:

.. code:: robotframework

   *** Settings ***

   Library  Selenium2Library

   Suite Teardown  Close all browsers

   *** Variables ***

   ${BROWSER}  Firefox

   *** Test Cases ***

   Capture a screenshot of RobotFramework.org
       Open browser  http://robotframework.org/  browser=${BROWSER}
       Capture page screenshot  robotframework.png

Finally, to avoid the same screenshot being generated again and again, limit it
to be generated only once, by entering the following special
``robotframework``-directive.

.. code:: restructuredtext

   .. robotframework::
      :creates: robotframework.png

This will limit tests in this document to be run only when the files expected
to be created by Robot Framework do not exist.

.. robotframework::
   :creates: robotframework.png

Isn't it beautiful:

.. image:: robotframework.png
   :width: 600

.. Links:
.. _sphinxcontrib-robotframework:
   http://pypi.python.org/pypi/sphinxcontrib-robotframework
.. _robotframework-selenium2library:
   http://pypi.python.org/pypi/robotframework-selenium2library
