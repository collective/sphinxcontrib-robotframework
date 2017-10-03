Changelog
=========

0.7.0 (2017-10-03)
------------------

- Fix issue where plugin was broken on Sphinx >= 1.5
  [datakurre]

- Fix issue where robot framework test suites without tests were run
  [datakurre]

0.6.1 (2016-09-25)
------------------

- Fix to provide default value (False) when checking for nitpicky mode.
  [datakurre]

0.6.0 (2016-09-25)
------------------

- Add support for Sphinx nitpicky-mode.

  When nitpicky mode is enabled, failing Robot Framework test in docs will
  raise Sphinx error and leave Robot Framework log file into docs src
  directory.
  [datakurre]

0.5.1 (2015-07-24)
------------------

- Fix issue where non-ascii characters caused build failures
  [datakurre]

0.5.0 (2014-12-24)
------------------

- Add to persist log of successfully run Robot Framework tests and to not
  re-run them until they are changed (or build is cleared).
  This obsoletes ``.. robotframework:: :creates:`` -behavior.
  [datakurre]

0.4.4 (2014-07-20)
------------------

- Update documentation
  [datakurre]

0.4.3 (2014-02-10)
------------------

- Add global 'quiet' option to drop all robot syntax from sphinx output
  [datakurre]

0.4.2 (2013-09-30)
------------------

- Fix to keep working with robotframework < 2.8.x
  [datakurre]

0.4.1 (2013-09-30)
------------------

- Add test suite validation and skip running test suites without test cases
  [datakurre]

0.4.0 (2013-09-29)
------------------

- Add support for overriding robot variables using ROBOT\_-prefixed environment
  variables [datakurre]

0.3.1 (2013-09-21)
------------------

- Fix issue in Sphinx's image processing after test has been run
  [datakurre]
