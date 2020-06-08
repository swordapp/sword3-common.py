from unittest import TestCase

from sword3common.models.metadata import Metadata
from sword3common import constants


class TestMetadata(TestCase):
    def test_01_metadata(self):
        m = Metadata()
        m.add_field("whatever", "value")
        m.add_dc_field("creator", "me")
        m.add_dc_field("dc:contributor", "them")
        m.add_dcterms_field("provenance", "here")
        m.add_dcterms_field("dcterms:modified", "now")

        assert m.get_field("whatever") == "value"
        assert m.get_dc_field("dc:creator") == "me"
        assert m.get_dc_field("contributor") == "them"
        assert m.get_dcterms_field("dcterms:provenance") == "here"
        assert m.get_dcterms_field("modified") == "now"

        assert m.data.get("@context") == constants.JSON_LD_CONTEXT
        self.assertEqual(constants.DocumentType.Metadata, m.data.get("@type"))

        m.verify_against_struct()
        m.apply_struct()

        assert m.get_field("whatever") == "value"
        assert m.get_dc_field("dc:creator") == "me"
        assert m.get_dc_field("contributor") == "them"
        assert m.get_dcterms_field("dcterms:provenance") == "here"
        assert m.get_dcterms_field("modified") == "now"
