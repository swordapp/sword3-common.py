from unittest import TestCase

from sword3common.models.service import ServiceDocument
from sword3common.test.fixtures.service import ServiceFixtureFactory
from sword3common.lib.seamless import SeamlessException
from sword3common import constants


class TestService(TestCase):
    def test_01_service_document(self):
        s = ServiceDocument()

        # a full one
        source = ServiceFixtureFactory.service_document()
        try:
            s = ServiceDocument(source)

            subs = s.services
            assert len(subs) == 1
            assert isinstance(subs[0], ServiceDocument)

            assert s.data.get("@context") == constants.JSON_LD_CONTEXT
            assert s.data.get("@type") == constants.DocumentType.ServiceDocument

        except SeamlessException as e:
            raise Exception(e.message)

        s.__seamless__.set_single("whatever", "junk data")
        with self.assertRaises(SeamlessException):
            s.verify_against_struct()
