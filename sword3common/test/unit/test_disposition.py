from unittest import TestCase

from sword3common.lib.disposition import ContentDisposition


class TestMetadata(TestCase):
    def test_01_disposition(self):
        cd = ContentDisposition.metadata_upload()
        assert cd.serialise() == "attachment; metadata=true"

        cd = ContentDisposition.binary_upload("simple.txt")
        assert cd.serialise() == "attachment; filename=simple.txt"

        cd = ContentDisposition.binary_upload("妇生孩.txt")
        assert cd.serialise() == "attachment; filename*=妇生孩.txt"

        cd = ContentDisposition.package_upload("simple.txt")
        assert cd.serialise() == "attachment; filename=simple.txt"

        cd = ContentDisposition.package_upload("妇生孩.txt")
        assert cd.serialise() == "attachment; filename*=妇生孩.txt"
