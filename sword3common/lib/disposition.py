from sword3common import constants

class ContentDisposition(object):
    def __init__(self, upload_type, content_type,
                 filename=None,
                 assembled_size=None,
                 segment_digest=None,
                 segment_count=None,
                 segment_size=None,
                 segment_number=None
            ):

        self._upload_type = upload_type
        self._content_type = content_type
        self._filename = filename
        self._size = assembled_size
        self._digest = segment_digest
        self._segment_count = segment_count
        self._segment_size = segment_size
        self._segment_number = segment_number

    @classmethod
    def metadata_upload(cls):
        return ContentDisposition(constants.DISPOSITION_DEPOSIT, constants.DISPOSITION_CONTENT_MD)

    @classmethod
    def binary_upload(cls, filename):
        return ContentDisposition(constants.DISPOSITION_DEPOSIT, constants.DISPOSITION_CONTENT_BINARY, filename=filename)

    @classmethod
    def package_upload(cls, filename):
        return ContentDisposition(constants.DISPOSITION_DEPOSIT, constants.DISPOSITION_CONTENT_PACKAGE, filename=filename)

    def serialise(self):
        disp_type = "attachment"
        if self._upload_type == constants.DISPOSITION_SEGMENT_INIT:
            disp_type = "segment-init"
        elif self._upload_type == constants.DISPOSITION_FILE_SEGMENT:
            disp_type = "segment"

        params = []
        if self._content_type in [constants.DISPOSITION_CONTENT_MD, constants.DISPOSITION_CONTENT_MDBR]:
            params.append("metadata=true")

        if self._content_type in [constants.DISPOSITION_CONTENT_BR, constants.DISPOSITION_CONTENT_MDBR]:
            params.append("by-reference=true")

        if self._content_type in [constants.DISPOSITION_CONTENT_BINARY, constants.DISPOSITION_CONTENT_PACKAGE]:
            try:
                self._filename.encode("iso-8859-1")
                params.append("filename={x}".format(x=self._filename))
            except UnicodeEncodeError:
                params.append("filename*={x}".format(x=self._filename))

        if disp_type == "segment-init":
            params.append("size={x}".format(x=self._size))
            params.append("digest={x}".format(x=self._digest))
            params.append("segment_count={x}".format(x=self._segment_count))
            params.append("segment_size={x}".format(x=self._segment_size))
        elif disp_type == "segment":
            params.append("segment_number={x}".format(x=self._segment_number))

        return "{x}; {y}".format(x=disp_type, y="; ".join(params))

    def __str__(self):
        return self.serialise()