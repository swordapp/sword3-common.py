from copy import deepcopy

class StatusFixtureFactory(object):

    @classmethod
    def status_document(self):
        return deepcopy(STATUS_DOC)


STATUS_DOC = {
    "@context" : "https://swordapp.github.io/swordv3/swordv3.jsonld",

    "@id" : "http://example.com/object/1",
    "@type" : "Status",
    "eTag" : "...",

    "metadata" : {
        "@id" : "http://www.myorg.ac.uk/sword3/object1/metadata",
        "eTag" : "..."
    },
    "fileSet" : {
        "@id" : "http://www.myorg.ac.uk/sword3/object1/fileset",
        "eTag" : "..."
    },

    "service" : "http://swordapp.org/deposit/43",

    "state" : [
        {
            "@id" : "http://purl.org/net/sword/3.0/state/inProgress",
            "description" : "the item is currently inProgress"
        }
    ],

    "actions" : {
        "getMetadata" : True,
        "getFiles" : True,
        "appendMetadata" : True,
        "appendFiles" : True,
        "replaceMetadata" : True,
        "replaceFiles" : True,
        "deleteMetadata" : True,
        "deleteFiles" : True,
        "deleteObject" : True
    },

    "lastAction" : {
        "timestamp" : "2019-01-01T00:00:00Z",
        "log" : "description of the event that occurred, with any verbose information",
        "treatment" : {
            "@id" : "http://www.myorg.ac.uk/treatment",
            "description" : "treatment description"
        }
    },

    "links" : [
        {
            "@id" : "http://www.myorg.ac.uk/col1/mydeposit.html",
            "rel" : ["alternate"],
            "contentType" : "text/html"
        },
        {
            "@id" : "http://www.myorg.ac.uk/sword3/object1/package.zip",
            "rel" : ["http://purl.org/net/sword/3.0/terms/originalDeposit"],
            "contentType" : "application/zip",
            "packaging" : "http://purl.org/net/sword/3.0/package/SimpleZip",
            "depositedOn" : "2019-01-01T00:00:00Z",
            "depositedBy" : "[user identifier]",
            "depositedOnBehalfOf" : "[user identifier]",
            "byReference" : "http://www.otherorg.ac.uk/by-reference/file.zip",
            "status" : "http://purl.org/net/sword/3.0/filestate/ingested",
            "log" : "[any information associated with the deposit that the client should know]"
        },
        {
            "@id" : "http://www.myorg.ac.uk/sword3/object1/file1.pdf",
            "rel" : [
                "http://purl.org/net/sword/3.0/terms/fileSetFile",
                "http://purl.org/net/sword/3.0/terms/derivedResource"
            ],
            "contentType" : "application/pdf",
            "derivedFrom" : "http://www.myorg.ac.uk/sword3/object1/package.zip",
            "dcterms:relation" : "http://www.myorg.ac.uk/repo/123456789/file1.pdf",
            "dcterms:replaces" : "http://www.myorg.ac.uk/sword3/object1/versions/file1.1.pdf",
            "eTag" : "..."
        },
        {
            "@id" : "http://www.myorg.ac.uk/sword3/object1/package.1.zip",
            "rel" : ["http://purl.org/net/sword/terms/packagedContent"],
            "contentType" : "application/zip",
            "packaging" : "http://purl.org/net/sword/3.0/package/SimpleZip"
        },
        {
            "@id" : "http://www.swordserver.ac.uk/col1/mydeposit/metadata.xml",
            "rel" : ["http://purl.org/net/sword/3.0/terms/formattedMetadata"],
            "contentType" : "text/json",
            "metadataFormat" : "http://purl.org/net/sword/3.0/types/Metadata"
        },
        {
            "@id" : "http://www.myorg.ac.uk/sword3/object1/versions/file1.1.pdf",
            "rel" : ["http://purl.org/net/sword/3.0/terms/derivedResource"],
            "contentType" : "application/pdf",
            "dcterms:isReplacedBy" : "http://www.myorg.ac.uk/sword3/object1/file1.pdf",
            "versionReplacedOn" : "2019-01-01T00:00:00Z"
        },
        {
            "@id" : "http://www.myorg.ac.uk/sword3/object1/reference.zip",
            "rel" : [
                "http://purl.org/net/sword/3.0/terms/byReferenceDeposit",
                "http://purl.org/net/sword/3.0/terms/originalDeposit",
                "http://purl.org/net/sword/3.0/terms/fileSetFile"
            ],
            "byReference" : "http://www.otherorg.ac.uk/by-reference/file2.zip",
            "log" : "Any information on the download, especially if it failed",
            "eTag" : "...",
            "status" : "http://purl.org/net/sword/3.0/filestate/ingested"
        }
    ],

    "forwarding" : [
        {
            "@id" : "http://www.otherorg.ac.uk/sword3/object12",

            "links" : [
                {
                    "@id" : "http://www.otherorg.ac.uk/col2/yourdeposit.html",
                    "rel" : ["alternate"],
                    "contentType" : "text/html"
                }
            ]
        }
    ]
}