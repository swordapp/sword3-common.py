from sword3common.lib.dataobj import DataObj

class ServiceDocument(DataObj):
    def __init__(self, raw=None):
        super(ServiceDocument, self).__init__(raw, struct=SERVICE_STRUCT, expose_data=True)


SERVICE_STRUCT = {
    "fields" : {
        "@context" : {"coerce" : "unicode"},
        "@id" : {"coerce" : "unicode"},
        "@type" : {"coerce" : "unicode"},
        "dc:title" : {"coerce" : "unicode"},
        "dcterms:abstract" : {"coerce" : "unicode"},
        "root" : {"coerce" : "unicode"},
        "acceptDeposits" : {"coerce" : "bool"},
        "version" : {"coerce" : "unicode", "allowed_values" : ["http://purl.org/net/sword/3.0"]},
        "maxUploadSize" : {"coerce" : "integer"},
        "maxByReferenceSize" : {"coerce" : "integer"},
        "maxAssembledSize" : {"coerce" : "integer"},
        "maxSegments" : {"coerce" : "integer"},
        "staging" : {"coerce" : "unicode"},
        "stagingMaxIdle" : {"coerce" : "integer"},
        "byReferenceDeposit" : {"coerce" : "bool"},
        "onBehalfOf" : {"coerce" : "bool"},
        "parent" : {"coerce" : "unicode"}
    },
    "lists" : {
        "accept" : {"contains" : "field", "coerce" : "unicode"},
        "acceptArchiveFormat" : {"contains" : "field", "coerce" : "unicode"},
        "acceptPackaging" : {"contains" : "field", "coerce" : "unicode"},
        "acceptMetadata" : {"contains" : "field", "coerce" : "unicode"},
        "digest" : {"contains" : "field", "coerce" : "unicode"},
        "authentication" : {"contains" : "field", "coerce" : "unicode"},
        "services" : {"contains" : "object"}
    },
    "objects" : [
        "collectionPolicy",
        "treatment"
    ],

    "structs" : {
        "collectionPolicy" : {
            "fields" : {
                "@id" : {"coerce" : "unicode"},
                "description" : {"coerce" : "unicode"}
            }
        },
        "treatment" : {
            "fields" : {
                "@id" : {"coerce" : "unicode"},
                "description" : {"coerce" : "unicode"}
            }
        }
    }
}

from sword3common.lib.seamless import SeamlessMixin, SeamlessData

def makeSeamlessService(raw):
    return SeamlessService(raw)

def makeCP(raw):
    return SeamlessData(raw)

def extractCP(refined):
    return refined.data

class SeamlessService(SeamlessMixin):
    __SEAMLESS_STRUCT__ = SERVICE_STRUCT

    __SEAMLESS_PROPERTIES__ = {
        "maxUploadSize" : {"path" : "maxUploadSize"},
        "random" : {"path" : "doesnt.exist"},
        "services" : {"path" : "services", "wrapper": makeSeamlessService},
        "collection_policy" : {"path" : "collectionPolicy", "wrapper" : makeCP, "unwrapper" : extractCP}
    }

    def __init__(self, raw=None):
        super(SeamlessService, self).__init__(raw)

    @property
    def data(self):
        return self.__seamless__.data