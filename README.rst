===========
PyKeyMapper
===========

.. image:: https://readthedocs.org/projects/pykeymapper/badge/?version=latest
   :target: https://pykeymapper.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://gitlab.com/sluenenglish/pykeymapper/badges/master/pipeline.svg
   :target: https://gitlab.com/sluenenglish/pykeymapper/-/commits/master
   :alt: Gitlab pipeline status (branch)

.. image:: https://img.shields.io/pypi/v/pykeymapper
   :target: https://pypi.org/project/pykeymappe
   :alt: PyPI


PyKeyMapper is an unofficial plugin for `interception tools`_.
It provides a set of utilities to easily create executables which manipulate input to create advanced keyboard mappings.

.. _`interception tools`: https://gitlab.com/interception/linux/tools/

A set of preconfigured executables are supplied for inspiration and convenience,
but it is easy (and encouraged) to make your own.

Preconfigured keyboard mappings can used via the command line interface:

.. code-block:: console

    $ pykeymapper --help

    Usage: pykeymapper [OPTIONS] COMMAND [ARGS]...

      PyKeyMapper - A tool to customise your keyboard

    Options:
      --help  Show this message and exit.

    Commands:
      alt-brackets        Turn alt key into "Bracket Button"
      backslash2shift     Make backslash shift when pressed with another key
      forwardslash2shift  Make forward slash shift when pressed with another key
      special-space       Turn space into "Special Character key"


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

