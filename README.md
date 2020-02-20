# SWORDv3 Common Library

[![Build Status](https://travis-ci.org/swordapp/sword3-common.py.svg?branch=master)](https://travis-ci.org/swordapp/sword3-common.py) [![codecov](https://codecov.io/gh/swordapp/sword3-common.py/branch/master/graph/badge.svg)](https://codecov.io/gh/swordapp/sword3-common.py)

This library provides a set of resources which can be used by any SWORD Python implementation, both client and server-side.

It consists of:

* A set of model objects that can represent the key document types used by SWORDv3 (`sword3common.models`)
* A set of constants that are used throughout the specification, such as URIs (`sword3common.constants`)
* A set of exceptions which a client or server may be required to raise or handle (`sword3common.exceptions`)
* Some common test fixtures and document examples which can be used for testing clients and servers (`sword3common.test.fixtures`)

## Example usage

Create model objects via their APIs

```python
import json
from sword3common import (
    Metadata, 
    ByReference, 
    MetadataAndByReference, 
    )

# create a metadata record containing simple DC, full DCMI terms, and a custom field
metadata = Metadata()
metadata.add_dc_field("creator", "Richard")
metadata.add_dcterms_field("rights", "CC0")
metadata.add_field("custom", "value")

# Create a ByReference object with a single file
br = ByReference()
br.add_file("http://example.com/file.pdf",
            "file.pdf",
            "application/pdf",
            True)

# Combine them both into a MetadataAndByReference object:
mdbr = MetadataAndByReference(metadata, br)

# To access the data and serialise them for delivery:
payload = json.dumps(mdbr.data)
```

Read them from raw data:

```python
import json
from sword3common import (
    Metadata, 
    ByReference 
    )

metadata_raw = "..."        # JSON string of metadata
br_raw = "..."              # JSON string of by reference data

# read them both into their objects
metadata = Metadata(json.loads(metadata_raw))
br = ByReference(json.loads(br_raw))

# read the values back out
assert metadata.get_dc_field("creator") == "Richard"
assert metadata.get_dcterms_field("rights") == "CC0"
assert metadata.get_field("custom") == "value"
```

## Notes on limitations

NOTE that all the objects in the library have only the features that were required to deliver the reference
implementation, so there are not full object APIs for every interaction that you may wish to use.  This library
will need to be expanded in time to be a fully featured common library. 