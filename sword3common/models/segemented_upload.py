from sword3common.lib.seamless import SeamlessMixin
from sword3common import constants

SEGMENTED_FILE_UPLOAD_STRUCT = {
    "fields": {
        "@context": {"coerce": "unicode"},
        "@id": {"coerce": "unicode"},
        "@type": {"coerce": "unicode"},
    },
    "objects": ["segments"],
    "structs": {
        "segments": {
            "fields": {
                "size": {"coerce": "integer"},
                "segment_size": {"coerce": "integer"},
            },
            "lists": {
                "received": {"contains": "field", "coerce": "integer"},
                "expecting": {"contains": "field", "coerce": "integer"},
            },
        }
    },
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

    @property
    def received(self):
        return self.__seamless__.get_list("segments.received")

    @received.setter
    def received(self, val):
        self.__seamless__.set_with_struct("segments.received", val)

    @property
    def expecting(self):
        return self.__seamless__.get_list("segments.expecting")

    @expecting.setter
    def expecting(self, val):
        self.__seamless__.set_with_struct("segments.expecting", val)

    @property
    def size(self):
        return self.__seamless__.get_single("segments.size")

    @size.setter
    def size(self, val):
        self.__seamless__.set_with_struct("segments.size", val)

    @property
    def segment_size(self):
        return self.__seamless__.get_single("segments.segment_size")

    @segment_size.setter
    def segment_size(self, val):
        self.__seamless__.set_with_struct("segments.segment_size", val)
