Document with an annotated screenshot
=====================================

While Selenium_ has built-in support for capturing whole page screenshots, usually screenshots must be cropped and some times also annotated to make them useful in a documentation.

.. _Selenium: http://docs.seleniumhq.org/

A Robot Framework library called Selenium2Screenshots_ provides a collection of re-usable keywords for cropping and annotating screenshots.

.. _Selenium2Screenshots: http://pypi.python.org/pypi/robotframework-selenium2screenshots

A cropped and annotated screenshot could look like this:

.. figure:: robotframework.png
.. code:: robotframework
   :class: hidden

   *** Settings ***

   Library  Selenium2Library
   Library  Selenium2Screenshots

   Suite Teardown  Close all browsers

   *** Variables ***

   ${BROWSER}  Firefox

   *** Keywords ***

   Highlight heading
       [Arguments]  ${locator}
       Update element style  ${locator}  margin-top  0.75em
       Highlight  ${locator}

   *** Test Cases ***

   Take an annotated screenshot of RobotFramework.org
       Open browser  http://robotframework.org/  browser=${BROWSER}

       Highlight heading   css=#header h1

       ${note1} =  Add pointy note
       ...    css=#header
       ...    This screenshot was generated using Robot Framework and Selenium.
       ...    width=250  position=bottom
       Capture and crop page screenshot  robotframework.png
       ...    css=#header  ${note1}

.. note::

   The image cropping feature for **robotframework-selenium2screenshots**
   requires PIL_ or Pillow_.

.. _PIL: https://pypi.python.org/pypi/PIL
.. _Pillow: https://pypi.python.org/pypi/Pillow
