from unittest import TestCase

from sword3common.models.service import ServiceDocument, SeamlessService
from sword3common.test.fixtures.service import ServiceFixtureFactory
from sword3common.lib.seamless import SeamlessException, SeamlessData

class TestService(TestCase):
    def test_01_service(self):
        # construct a blank one
        s = ServiceDocument()

        # a full one
        source = ServiceFixtureFactory.service_document()
        s = ServiceDocument(source)

        assert s.maxUploadSize == 16777216000

    def test_02_seamless(self):
        s = SeamlessService()

        # a full one
        source = ServiceFixtureFactory.service_document()
        try:
            s = SeamlessService(source)

            assert s.maxUploadSize == 16777216000
            assert s.random is None

            with self.assertRaises(AttributeError):
                assert s.whatever == "hello"

            subs = s.services
            assert len(subs) == 1
            assert isinstance(subs[0], SeamlessService)

            cp = s.collection_policy
            assert isinstance(cp, SeamlessData)

            cp.data["description"] = "a new description"
            s.collection_policy = cp
            cp2 = s.collection_policy
            assert cp2.data["description"] == "a new description"

            s.maxUploadSize = 6
            assert s.maxUploadSize == 6

        except SeamlessException as e:
            raise Exception(e.message)