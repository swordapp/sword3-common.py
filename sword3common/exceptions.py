from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import cast, Dict, Tuple, Type, Optional

from .lib.seamless import SeamlessException


class SwordExceptionMeta(type):
    _registry: Dict[Tuple[int, Optional[str]], Type[SwordException]] = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if hasattr(cls, "status_code") and hasattr(cls, "name"):
            cls = cast(Type[SwordException], cls)
            # If this is the first time we've seen this status code, record it as the only exception for this code,
            # irrespective of SWORD exception name. If we've seen it before, remove it.
            if not any(True for status_code, name in cls._registry if status_code == cls.status_code):
                cls._registry[(cls.status_code, None)] = cls
            else:
                cls._registry.pop((cls.status_code, None), None)

                cls._registry[(cls.status_code, cls.name)] = cls
        return cls


class SwordException(Exception, metaclass=SwordExceptionMeta):

    status_code: int
    name: str
    reason: str

    @classmethod
    def for_status_code_and_name(cls, status_code: int, name: Optional[str]):
        return cls._registry[(status_code, name)]

    def __init__(self, message: str = None, *, response=None):
        self.message = message
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.response = response


class UnexpectedSwordException(SwordException):
    def __init__(self, *args, status_code: int, name: Optional[str], **kwargs):
        self.status_code = status_code
        self.name = name
        super().__init__(*args, **kwargs)


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


class ByReferenceNotAllowed(SwordException):
    status_code = HTTPStatus.PRECONDITION_FAILED
    name = "ByReferenceNotAllowed"
    reason = "The client attempted to carry out a By-Reference deposit on a server which does not support it"


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


class MaxAssembledSizeExceeded(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "MaxAssembledSizeExceeded"
    reason = "During a segmented upload initialisation, the client specified a total file size which is larger than the maximum assembled file size supported by the server"


class MaxUploadSizeExceeded(SwordException):
    status_code = HTTPStatus.REQUEST_ENTITY_TOO_LARGE
    name = "MaxUploadSizeExceeded"
    reason = "The request supplied body content which is larger than that supported by the server."


class MetadataFormatNotAcceptable(SwordException):
    status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    name = "MetadataFormatNotAcceptable"
    reason = "The Metadata-Format header specifies a metadata format for the request which is in a format that the server cannot accept"


class MethodNotAllowed(SwordException):
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    name = "MethodNotAllowed"
    reason = "The request is for a method on a resource that is not permitted. This may be permanent, temporary, and may depend on the client’s credentials"


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


class SegmentedUploadTimedOut(SwordException):
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    name = "SegmentedUploadTimedOut"
    reason = "The client's segmented upload URL has timed out.  Servers MAY respond to this with a 404 and no explanation also."


class SegmentLimitExceeded(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "SegmentLimitExceeded"
    reason = "During a segmented upload initialisation, the client specified a total number of intended segments which is larger than the limit specified by the server"


class UnexpectedSegment(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "UnexpectedSegment"
    reason = "The client sent a segment that the server was not expecting; in particular the server may have recieved all the segments it was expecting, and this is an extra one"


class ValidationFailed(SwordException):
    status_code = HTTPStatus.BAD_REQUEST
    name = "ValidationFailed"
    reason = "The server could not validate the structure of the incoming content against its expected schema.  This may include the JSON schema of the SWORD documents, the metadata held within those documents, or the expected structure of packaged content."
