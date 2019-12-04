from unittest import TestCase

from sword3common.models.service import ServiceDocument
from sword3common.test.fixtures.service import ServiceFixtureFactory
from sword3common.lib.seamless import SeamlessException

class TestService(TestCase):
    def test_01_service_document(self):
        s = ServiceDocument()

        # a full one
        source = ServiceFixtureFactory.service_document()
        try:
            s = ServiceDocument(source)

            assert s.maxUploadSize == 16777216000
            subs = s.services
            assert len(subs) == 1
            assert isinstance(subs[0], ServiceDocument)

            s.maxUploadSize = 6
            assert s.maxUploadSize == 6

        except SeamlessException as e:
            raise Exception(e.message)