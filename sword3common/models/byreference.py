from sword3common.lib.seamless import SeamlessMixin
from sword3common import constants, ContentDisposition

import typing

BY_REFERENCE_STRUCT = {
    "fields": {"@context": {"coerce": "unicode"}, "@type": {"coerce": "unicode"}},
    "lists": {"byReferenceFiles": {"contains": "object"}},
    "structs": {
        "byReferenceFiles": {
            "fields": {
                "@id": {"coerce": "unicode"},
                "contentType": {"coerce": "unicode"},
                "contentLength": {"coerce": "integer"},
                "contentDisposition": {"coerce": "unicode"},
                "packaging": {"coerce": "unicode"},
                "digest": {"coerce": "unicode"},
                "ttl": {"coerce": "datetime"},
                "dereference": {"coerce": "bool"},
            }
        }
    },
}


class ByReference(SeamlessMixin):
    __SEAMLESS_STRUCT__ = BY_REFERENCE_STRUCT

    __SEAMLESS_ALLOW_OTHER_FIELDS__ = False

    def __init__(self, raw=None):
        super(ByReference, self).__init__(raw)

        # set the fixed attributes of this object
        context = self.__seamless__.get_single("@context")
        if context is None:
            self.__seamless__.set_single("@context", constants.JSON_LD_CONTEXT)

        typ = self.__seamless__.get_single("@type")
        if typ is None:
            self.__seamless__.set_single("@type", constants.DocumentType.ByReference)

    @property
    def data(self):
        return self.__seamless__.data

    def add_file(
        self,
        url,
        filename,
        content_type,
        dereference,
        content_length=None,
        packaging=None,
        digest=None,
        ttl=None,
    ):
        cd = ContentDisposition.binary_upload(filename).serialise()
        packaging = packaging if packaging is not None else constants.PACKAGE_BINARY

        obj = {
            "@id": url,
            "contentType": content_type,
            "dereference": dereference,
            "contentDisposition": cd,
            "packaging": packaging,
        }

        if content_length is not None:
            obj["contentLength"] = content_length

        if digest is not None:
            obj["digest"] = self._make_digest_header(digest)

        if ttl is not None:
            obj["ttl"] = ttl

        self.__seamless__.add_to_list_with_struct("byReferenceFiles", obj)

    def _make_digest_header(self, digest: typing.Dict[str, str]):
        digest_parts = []
        for k, v in digest.items():
            digest_parts.append("{x}={y}".format(x=k, y=v))
        return ", ".join(digest_parts)
