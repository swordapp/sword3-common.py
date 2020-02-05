# SWORDv3 Common Library

This library provides a set of resources which can be used by any SWORD Python implementation, both client and server-side.

It consists of:

* A set of model objects that can represent the key document types used by SWORDv3 (`sword3common.models`)
* A set of constants that are used throughout the specification, such as URIs (`sword3common.constants`)
* A set of exceptions which a client or server may be required to raise or handle (`sword3common.exceptions`)
* Some common test fixtures and document examples which can be used for testing clients and servers (`sword3common.test.fixtures`)
