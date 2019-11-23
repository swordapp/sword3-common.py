from unittest import TestCase

from sword3common.models.service import ServiceDcument
from sword3common.test.fixtures.service import ServiceFixtureFactory

class TestService(TestCase):
    def test_01_service(self):
        # construct a blank one
        s = ServiceDcument()

        # a full one
        source = ServiceFixtureFactory.service_document()
        s = ServiceDcument(source)

        assert s.maxUploadSize == 16777216000