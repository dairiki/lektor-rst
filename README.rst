==========
lektor-rst
==========

This plugin for Lektor adds support for ReStructuredText files.


Configuration
=============

To adjust docutils parameters,
create a ``configs/rst.ini`` file in the Lektor project hierarchy.
The ``docutils`` section of the file will be used to control docutils output.

For example::

    [docutils]
    writer = html5
    initial_header_level = 1


Changelog
=========

0.4.0 - Unreleased
------------------

- Require docutils >= 0.21.
  [dairiki]

- Drop support for Python <= 3.8.
  [dairiki]

- Fix deprecation warning from docutils 0.22.
  [dairiki - Jeff Dairiki]


0.3.0 - 2023-02-21
------------------

- Drop support for Python <= 3.6.
  [fschulze]

- Fix deprecation warning from docutils 0.18.1.
  [glasnt - Katie McLaughlin]


0.2.0 - 2019-06-30
------------------

- Fix #5 - Allow configuration of docutils output options.
  [uyar, fschulze]

- Fix #3 - Underlines with dashes caused warnings.
  [uyar - H. Turgut Uyar, fschulze]

- Support Python 3.
  [uranusjr - Tzu-ping Chung, fschulze]


0.1.0 - 2016-01-18
------------------

- Initial release.
  [fschulze - Florian Schulze]
