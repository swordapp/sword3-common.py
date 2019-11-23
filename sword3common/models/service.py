from sword3common.lib.dataobj import DataObj

class ServiceDcument(DataObj):
    def __init__(self, raw=None):
        super(ServiceDcument, self).__init__(raw, struct=SERVICE_STRUCT, expose_data=True)


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