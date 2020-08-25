from sword3common.lib.disposition import ContentDisposition

from sword3common.models.metadata import Metadata
from sword3common.models.service import ServiceDocument
from sword3common.models.status import StatusDocument
from sword3common.models.byreference import ByReference
from sword3common.models.mdbr import MetadataAndByReference
from sword3common.models.segemented_upload import SegmentedFileUpload
from sword3common.models.error import Error

__all__ = [
    "ContentDisposition",
    "Metadata",
    "ServiceDocument",
    "StatusDocument",
    "ByReference",
    "MetadataAndByReference",
    "SegmentedFileUpload",
    "Error",
]

# Make this module the canonical import location for these members.
# This will provide shorter class path/names in the documentation.
for name in __all__:
    locals()[name].__module__ = __name__

from .version import __version__
