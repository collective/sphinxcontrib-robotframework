Document with a screenshot
==========================

The fun with **sphinxcontrib-robotframework** starts in using it together
with Selenium2Library_.

.. _Selenium2Library: https://github.com/rtomac/robotframework-selenium2library

These packages together  would allow you to navigate any website, take
screenshots when required and finally embed those screenshot into this very
Sphinx-documentation. All this with just ``sphinx-build``:

.. figure:: robotframework.png
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

Finally, to avoid the same screenshot being generated again and again, a
special ``robotframework``-directive (added by this package) can be used
to limit the tests to be executed only once (until the listed screenshot
is successfully generated):

.. code:: restructuredtext

   .. robotframework::
      :creates: robotframework.png

.. robotframework::
   :creates: robotframework.png
