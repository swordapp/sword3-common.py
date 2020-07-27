# SWORDv3 Common Library

[![Build Status](https://travis-ci.org/swordapp/sword3-common.py.svg?branch=master)](https://travis-ci.org/swordapp/sword3-common.py) [![codecov](https://codecov.io/gh/swordapp/sword3-common.py/branch/master/graph/badge.svg)](https://codecov.io/gh/swordapp/sword3-common.py)


[![Documentation Status](https://readthedocs.org/projects/sword3-commonpy/badge/?version=latest)](https://sword3-commonpy.readthedocs.io/en/latest/?badge=latest)

This library provides a set of resources which can be used by any SWORD Python implementation, both client and server-side.

It consists of:

* A set of model objects that can represent the key document types used by SWORDv3 (`sword3common.models`)
* A set of constants that are used throughout the specification, such as URIs (`sword3common.constants`)
* A set of exceptions which a client or server may be required to raise or handle (`sword3common.exceptions`)
* Some common test fixtures and document examples which can be used for testing clients and servers (`sword3common.test.fixtures`)

[Read the documentation](https://sword3-commonpy.readthedocs.io/en/latest/)