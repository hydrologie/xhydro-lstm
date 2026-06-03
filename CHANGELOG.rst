=========
Changelog
=========

..
    `Unreleased <https://github.com/hydrologie/xhydro-lstm>`_ (latest)
    ------------------------------------------------------------------

    Contributors: Trevor James Smith (:user:`Zeitsperre`).

    Changes
    ^^^^^^^
    * First functional version of the package. (:pull:`14`).
    * Updated the cookiecutter template to use the latest commit. (:pull:`131`):
        * Python 3.9 support has been dropped.
        * Replaced `tox.ini` with `tox.toml`.
        * Updated GitHub Actions workflows.
        * Updated base dependencies for CI workflows.
        * Now using Contributor Covenant v3.0 for the code of conduct.
        * Replaced `black`, `blackdoc`, and `isort` with `ruff` for code formatting and linting.
    * `xhydro-lstm` now has guidance documents on acceptable usages of AI and the expected methods of AI usage disclosure. See the documentation for more details. (#114).
    * Updated the cookiecutter template to use the latest commit. (:pull:`169`):
        * Adjusted the permissions for some workflows to address security issues.
        * Added the new "standard" AI disclosure guidance for code contributions.
        * Updated the ReadTheDocs configuration to use newer OS and conda images.
        * Modified ``make servedocs`` to use `sphinx-autobuild` (``make livehtml``).
        * Added guidance for maintainers on git commit signing and immutable releases.
        * Adjusted the source distribution inclusion/exclusion list.
        * Set `bump-my-version` to sign tags by default.

    Fixes
    ^^^^^
    * No change.

.. _changes_0.1.0:

`v0.1.1 <https://github.com/hydrologie/xhydro-lstm/tree/0.1.1>`_ (2025-03-10)
-----------------------------------------------------------------------------

Contributors: Trevor James Smith (:user:`Zeitsperre`), Richard Arsenault (:user:`richardarsenault`).

* First release on PyPI.

Changes
^^^^^^^
* First working version of `xhydro-lstm` with the LSTM utilities. (:pull:`14`)
* Generated the package using the cookiecutter template (`Ouranosinc/cookiecutter-pypackage <https://github.com/Ouranosinc/cookiecutter-pypackage>`_). (:issue:`1`, :pull:`13`)
