Version History
===============

v2.0.1 (28/09/2021)
-------------------
Bug Fixes
^^^^^^^^^
* Added ``requirements_dev.txt`` to manifest file because it is read by ``setup.py``.

v2.0.0 (27/09/2021)
-------------------
Bug Fixes
^^^^^^^^^
N/A

Breaking Changes
^^^^^^^^^^^^^^^^
* Changed ``nc_interface`` sub-package to rely on ``xarray`` instead of ``cdms2``.

New Features
^^^^^^^^^^^^
* Changed ``nc_interface`` sub-package to rely on ``xarray`` instead of ``cdms2``.
* Added unit tests for all new code in ``tests``
  * Run tests with: ``pytest tests``

v1.1.4 (2017-10-13)
-------------------

Overview
^^^^^^^^

* includes unit tests
* includes ``nc_interface`` to netCDF - using `cdms2` library

