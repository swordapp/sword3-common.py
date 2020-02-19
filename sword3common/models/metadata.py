from sword3common.lib.seamless import SeamlessMixin
from sword3common import constants

METADATA_STRUCT = {
    "fields": {
        "@context": {"coerce": "unicode"},
        "@id": {"coerce": "unicode"},
        "@type": {"coerce": "unicode"},
    }
}


class Metadata(SeamlessMixin):
    __SEAMLESS_STRUCT__ = METADATA_STRUCT

    __SEAMLESS_ALLOW_OTHER_FIELDS__ = True

    def __init__(self, raw=None):
        super(Metadata, self).__init__(raw)

        # set the fixed attributes of this object
        context = self.__seamless__.get_single("@context")
        if context is None:
            self.__seamless__.set_single("@context", constants.JSON_LD_CONTEXT)

        typ = self.__seamless__.get_single("@type")
        if typ is None:
            self.__seamless__.set_single("@type", constants.DocumentType.Metadata)

    @property
    def data(self):
        return self.__seamless__.data

    def add_dc_field(self, field, value):
        if not field.startswith("dc:"):
            field = "dc:" + field
        self.add_field(field, value)

    def add_dcterms_field(self, field, value):
        if not field.startswith("dcterms:"):
            field = "dcterms:" + field
        self.add_field(field, value)

    def add_field(self, field, value):
        self.__seamless__.set_single(field, value)

    def get_dc_field(self, field):
        if not field.startswith("dc:"):
            field = "dc:" + field
        return self.get_field(field)

    def get_dcterms_field(self, field):
        if not field.startswith("dcterms:"):
            field = "dcterms:" + field
        return self.get_field(field)

    def get_field(self, field):
        return self.__seamless__.get_single(field)
