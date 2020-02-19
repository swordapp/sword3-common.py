from unittest import TestCase

from sword3common.lib.seamless import SeamlessException
from sword3common.models.status import StatusDocument
from sword3common.test.fixtures.status import StatusFixtureFactory
from sword3common.lib.seamless import SeamlessException
from sword3common import constants


class TestStatus(TestCase):
    def test_01_status_document(self):
        # a full one
        source = StatusFixtureFactory.status_document()
        try:
            StatusDocument(source)
        except SeamlessException as e:
            raise Exception(e.message)
