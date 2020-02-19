from sword3common.models.metadata import Metadata
from sword3common.models.byreference import ByReference


class MetadataAndByReference:
    def __init__(self, metadata: Metadata, by_reference: ByReference):
        self._md = metadata
        self._br = by_reference

    @property
    def data(self):
        return {"metadata": self._md.data, "by-reference": self._br.data}

    @property
    def metadata(self):
        return self._md

    @metadata.setter
    def metadata(self, metadata: Metadata):
        self._md = metadata

    @property
    def by_reference(self):
        return self._br

    @by_reference.setter
    def by_reference(self, by_reference: ByReference):
        self._br = by_reference
