from sword3common.lib.seamless import SeamlessMixin
from sword3common import constants

ERROR_STRUCT = {
    "fields": {
        "@context": {"coerce": "unicode"},
        "@type": {"coerce": "unicode"},
        "timestamp": {"coerce": "utcdatetime"},
        "error": {"coerce": "unicode"},
        "log": {"coerce": "unicode"},
    }
}


class Error(SeamlessMixin):
    __SEAMLESS_STRUCT__ = ERROR_STRUCT

    __SEAMLESS_ALLOW_OTHER_FIELDS__ = False

    def __init__(self, raw=None):
        super(Error, self).__init__(raw)

        # set the fixed attributes of this object
        context = self.__seamless__.get_single("@context")
        if context is None:
            self.__seamless__.set_single("@context", constants.JSON_LD_CONTEXT)

    @property
    def type(self):
        return self.__seamless__.get_single("@type")
