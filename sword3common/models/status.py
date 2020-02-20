from sword3common.lib.seamless import SeamlessMixin
from sword3common import constants

STATUS_STRUCT = {
    "fields": {
        "@context": {"coerce": "unicode"},
        "@id": {"coerce": "unicode"},
        "@type": {"coerce": "unicode"},
        "eTag": {"coerce": "unicode"},
        "service": {"coerce": "unicode"},
    },
    "lists": {
        "state": {"contains": "object"},
        "links": {"contains": "object"},
        "forwarding": {"contains": "object"},
    },
    "objects": ["metadata", "fileSet", "actions", "lastAction"],
    "required": [
        "@context",
        "@id",
        "@type",
        "actions",
        "fileSet",
        "metadata",
        "service",
        "state",
    ],
    "structs": {
        "metadata": {
            "fields": {"@id": {"coerce": "unicode"}, "eTag": {"coerce": "unicode"}}
        },
        "fileSet": {
            "fields": {"@id": {"coerce": "unicode"}, "eTag": {"coerce": "unicode"}},
            "required": ["@id"],
        },
        "state": {
            "fields": {
                "@id": {"coerce": "unicode"},
                "description": {"coerce": "unicode"},
            },
            "required": ["@id"],
        },
        "actions": {
            "fields": {
                "getMetadata": {"coerce": "bool"},
                "getFiles": {"coerce": "bool"},
                "appendMetadata": {"coerce": "bool"},
                "appendFiles": {"coerce": "bool"},
                "replaceMetadata": {"coerce": "bool"},
                "replaceFiles": {"coerce": "bool"},
                "deleteMetadata": {"coerce": "bool"},
                "deleteFiles": {"coerce": "bool"},
                "deleteObject": {"coerce": "bool"},
            },
            "required": [
                "getMetadata",
                "getFiles",
                "appendMetadata",
                "appendFiles",
                "replaceMetadata",
                "replaceFiles",
                "deleteMetadata",
                "deleteFiles",
                "deleteObject",
            ],
        },
        "lastAction": {
            "fields": {
                "timestamp": {"coerce": "datetime"},
                "log": {"coerce": "unicode"},
            },
            "objects": ["treatment"],
            "structs": {
                "treatment": {
                    "fields": {
                        "@id": {"coerce": "unicode"},
                        "description": {"coerce": "unicode"},
                    }
                }
            },
        },
        "links": {
            "fields": {
                "@id": {"coerce": "unicode"},
                "contentType": {"coerce": "unicode"},
                "packaging": {"coerce": "unicode"},
                "depositedOn": {"coerce": "datetime"},
                "depositedBy": {"coerce": "unicode"},
                "depositedOnBehalfOf": {"coerce": "unicode"},
                "byReference": {"coerce": "unicode"},
                "status": {"coerce": "unicode"},
                "log": {"coerce": "unicode"},
                "derivedFrom": {"coerce": "unicode"},
                "dcterms:relation": {"coerce": "unicode"},
                "dcterms:replaces": {"coerce": "unicode"},
                "dcterms:isReplacedBy": {"coerce": "unicode"},
                "eTag": {"coerce": "unicode"},
                "metadataFormat": {"coerce": "unicode"},
                "versionReplacedOn": {"coerce": "datetime"},
            },
            "lists": {"rel": {"contains": "field", "coerce": "unicode"}},
            "required": ["@id", "rel"],
        },
        "forwarding": {
            "fields": {"@id": {"coerce": "unicode"},},
            "lists": {"links": {"contains": "object"}},
            "structs": {
                "links": {
                    "fields": {
                        "@id": {"coerce": "unicode"},
                        "contentType": {"coerce": "unicode"},
                    },
                    "lists": {"rel": {"contains": "field", "coerce": "unicode"}},
                    "required": ["@id"],
                }
            },
        },
    },
}


class StatusDocument(SeamlessMixin):
    __SEAMLESS_STRUCT__ = STATUS_STRUCT

    __SEAMLESS_PROPERTIES__ = {}  # type: dict

    def __init__(self, raw=None):
        super(StatusDocument, self).__init__(raw)

        # set the fixed attributes of this object
        context = self.__seamless__.get_single("@context")
        if context is None:
            self.__seamless__.set_single("@context", constants.JSON_LD_CONTEXT)

        typ = self.__seamless__.get_single("@type")
        if typ is None:
            self.__seamless__.set_single("@type", constants.DocumentType.Status)

    @property
    def data(self):
        return self.__seamless__.data

    @property
    def object_url(self):
        return self.__seamless__.get_single("@id")

    @property
    def metadata_url(self):
        return self.__seamless__.get_single("metadata.@id")

    @property
    def fileset_url(self):
        return self.__seamless__.get_single("fileSet.@id")

    @property
    def links(self):
        return self.__seamless__.get_list("links")

    def list_links(self, rels):
        return [link for link in self.links if set(link["rel"]) & set(rels)]
