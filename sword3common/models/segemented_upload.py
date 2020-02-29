from sword3common.lib.seamless import SeamlessMixin
from sword3common import constants

SEGMENTED_FILE_UPLOAD_STRUCT = {
    "fields" : {
        "@context" : {"coerce" : "unicode"},
        "@id" : {"coerce" : "unicode"},
        "@type" : {"coerce" : "unicode"}
    },
    "objects" : [
        "segments"
    ],
    "structs" : {
        "segments" : {
            "fields" : {
                "size" : {"coerce" : "integer"},
                "segment_size" : {"coerce" : "integer"}
            },
            "lists" : {
                "received" : {"contains" : "field", "coerce" : "integer"},
                "expecting" : {"contains" : "field", "coerce" : "integer"}
            }
        }
    }
}

class SegmentedFileUpload(SeamlessMixin):
    __SEAMLESS_STRUCT__ = SEGMENTED_FILE_UPLOAD_STRUCT

    __SEAMLESS_ALLOW_OTHER_FIELDS__ = False

    def __init__(self, raw=None):
        super(SegmentedFileUpload, self).__init__(raw)

        # set the fixed attributes of this object
        context = self.__seamless__.get_single("@context")
        if context is None:
            self.__seamless__.set_single("@context", constants.JSON_LD_CONTEXT)

        typ = self.__seamless__.get_single("@type")
        if typ is None:
            self.__seamless__.set_single("@type", constants.DocumentType.Temporary)