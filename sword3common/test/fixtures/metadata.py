from copy import deepcopy


class MetadataFixtureFactory(object):
    @classmethod
    def metadata(self):
        return deepcopy(METADATA)


METADATA = {
    "@context": "https://swordapp.github.io/swordv3/swordv3.jsonld",
    "@id": "http://example.com/object/10/metadata",
    "@type": "Metadata",
    "dc:title": "The title",
    "dcterms:abstract": "This is my abstract",
    "dc:contributor": "A.N. Other",
}
