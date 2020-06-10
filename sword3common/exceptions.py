# from __future__ import annotations
import datetime
from http import HTTPStatus
from typing import cast, Dict, Tuple, Type, Optional

from .lib.seamless import SeamlessException
from . import constants


class SwordExceptionMeta(type):
    _registry = {}  #: Dict[Tuple[int, Optional[str]], Type[SwordException]] = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if hasattr(cls, "status_code") and hasattr(cls, "name"):
            cls._registry[(cls.status_code, cls.name)] = cls
        return cls


class SwordException(Exception, metaclass=SwordExceptionMeta):

    status_code = None  #: int
    name = None  #: str
    reason = None  #: str
    contexts = []

    @classmethod
    def for_status_code_and_name(cls, status_code: int, type_name: Optional[str]):
        if type_name is not None:
            return cls._registry[(status_code, type_name)]
        else:
            opts = cls.for_status_code(status_code)
            if len(opts) == 1:
                return opts[1]
        return None

    @classmethod
    def for_status_code(cls, status_code: int):
        return [v for k, v in cls._registry.items() if k[0] == status_code]

    @classmethod
    def for_type(cls, type_name: str):
        opt = [v for k, v in cls._registry.items() if k[1] == type_name]
        if len(opt) > 0:
            return opt[0]
        return None

    def __init__(
        self, message: str = None, *, response=None, error_doc=None, request_url=None
    ):
        self.message = message
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.response = response
        self.error_doc = error_doc
        self.request_url = request_url


class AmbiguousSwordException(SwordException):
    def __init__(self, *args, status_code: int, **kwargs):
        self.status_code = status_code
        super().__init__(*args, **kwargs)


class UnexpectedSwordException(SwordException):
    def __init__(self, *args, status_code: int, name: Optional[str], **kwargs):
        self.status_code = status_code
        self.name = name
        super().__init__(*args, **kwargs)


# Exceptions that can be raised by a client


class InvalidDataFromServer(SwordException):
    pass


# Exceptions that can be raised server-side


class NoCredentialsSupplied(SwordException):
    status_code = HTTPStatus.UNAUTHORIZED
    name = "NoCredentialsSupplied"
    reason = "The request did not supply credentials, when the server was expecting to authenticate the request."


class AuthenticationFailed(SwordException):
    status_code = HTTPStatus.FORBIDDEN
    name = "AuthenticationFailed"
    reason = "The request supplied invalid credentials, or no credentials, when the server was expecting to authenticate the request."


class BadRequest(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "BadRequest"
    reason = "The request did not meet the standard specified by the SWORD protocol. This error can be used when no other error is appropriate"


class ByReferenceFileSizeExceeded(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "ByReferenceFileSizeExceeded"
    reason = "The client supplied a By-Reference deposit file, which specified a file size which exceeded the server's limit"
    contexts = [constants.RequestContexts.ByReference]


class ByReferenceNotAllowed(SwordException):
    status_code = HTTPStatus.PRECONDITION_FAILED
    name = "ByReferenceNotAllowed"
    reason = "The client attempted to carry out a By-Reference deposit on a server which does not support it"
    contexts = [constants.RequestContexts.ByReference]


class ContentMalformed(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "ContentMalformed"
    reason = "The body content of the request was malformed in some way, such that the server cannot read it correctly."


class ContentTypeNotAcceptable(SwordException):
    status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    name = "ContentTypeNotAcceptable"
    reason = "The Content-Type header specifies a content type of the request which is in a format that the server cannot accept."


class DigestMismatch(SwordException):
    status_code = HTTPStatus.PRECONDITION_FAILED
    name = "DigestMismatch"
    reason = "One or more of the Digests that the server checked did not match the deposited content"


class ETagNotMatched(SwordException):
    status_code = HTTPStatus.PRECONDITION_FAILED
    name = "ETagNotMatched"
    reason = "The client supplied an If-Match header which did not match the current ETag for the resource being updated."


class ETagRequired(SwordException):
    status_code = HTTPStatus.PRECONDITION_FAILED
    name = "ETagRequired"
    reason = "The client did not supply an If-Match header, when one was required by the server"


class FormatHeaderMismatch(SwordException):
    status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    name = "FormatHeaderMismatch"
    reason = "The Metadata-Format or Packaging header does not match what the server found when looking at the Metadata or Packaged Content supplied in a request."


class InvalidSegmentSize(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "InvalidSegmentSize"
    reason = "The client sent a segment that was not the final segment, and was not the size that it indicated segments would be"
    contexts = [constants.RequestContexts.Temporary]


class MaxAssembledSizeExceeded(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "MaxAssembledSizeExceeded"
    reason = "During a segmented upload initialisation, the client specified a total file size which is larger than the maximum assembled file size supported by the server"
    contexts = [constants.RequestContexts.Temporary]


class MaxUploadSizeExceeded(SwordException):
    status_code = HTTPStatus.REQUEST_ENTITY_TOO_LARGE
    name = "MaxUploadSizeExceeded"
    reason = "The request supplied body content which is larger than that supported by the server."


class MetadataFormatNotAcceptable(SwordException):
    status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    name = "MetadataFormatNotAcceptable"
    reason = "The Metadata-Format header specifies a metadata format for the request which is in a format that the server cannot accept"
    contexts = [
        constants.RequestContexts.Metadata,
        constants.RequestContexts.MetadataAndByReference,
    ]


class MethodNotAllowed(SwordException):
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    name = "MethodNotAllowed"
    reason = "The request is for a method on a resource that is not permitted. This may be permanent, temporary, and may depend on the client’s credentials"


class NotFound(SwordException):
    status_code = HTTPStatus.NOT_FOUND
    name = "NotFound"
    reason = "The resource could not be found"


class Gone(NotFound):
    status_code = HTTPStatus.GONE
    name = "Gone"
    reason = "The resource used to exist at the given URL, but has been removed."


class OnBehalfOfNotAllowed(SwordException):
    status_code = HTTPStatus.PRECONDITION_FAILED
    name = "OnBehalfOfNotAllowed"
    reason = "The request contained an On-Behalf-Of header, although the server indicates that it does not support this."


class PackagingFormatNotAcceptable(SwordException):
    status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    name = "PackagingFormatNotAcceptable"
    reason = "The Packaging header specifies a packaging format for the request which is in a format that the server cannot accept"


class SegmentedUploadNotAllowed(SwordException):
    status_code = HTTPStatus.PRECONDITION_FAILED
    name = "SegmentedUploadNotAllowed"
    reason = "The client attempted to carry out a Segmented Upload on a server which does not support it"
    contexts = [constants.RequestContexts.SegmentInit]


class SegmentedUploadTimedOut(SwordException):
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    name = "SegmentedUploadTimedOut"
    reason = "The client's segmented upload URL has timed out.  Servers MAY respond to this with a 404 and no explanation also."
    contexts = [constants.RequestContexts.Temporary]


class SegmentLimitExceeded(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "SegmentLimitExceeded"
    reason = "During a segmented upload initialisation, the client specified a total number of intended segments which is larger than the limit specified by the server"
    contexts = [constants.RequestContexts.SegmentInit]


class UnexpectedSegment(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "UnexpectedSegment"
    reason = "The client sent a segment that the server was not expecting; in particular the server may have recieved all the segments it was expecting, and this is an extra one"
    contexts = [constants.RequestContexts.Temporary]


class ValidationFailed(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "ValidationFailed"
    reason = "The server could not validate the structure of the incoming content against its expected schema.  This may include the JSON schema of the SWORD documents, the metadata held within those documents, or the expected structure of packaged content."
