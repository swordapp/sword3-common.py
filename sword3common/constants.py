JSON_LD_CONTEXT = "https://swordapp.github.io/swordv3/swordv3.jsonld"

DISPOSITION_SEGMENT_INIT = "disposition_segment_init"
DISPOSITION_DEPOSIT = "disposition_deposit"
DISPOSITION_FILE_SEGMENT = "disposition_file_segment"

DISPOSITION_CONTENT_BINARY = "disposition_content_binary"
DISPOSITION_CONTENT_PACKAGE = "disposition_content_package"
DISPOSITION_CONTENT_SEGMENT = "disposition_content_segment"
DISPOSITION_CONTENT_MD = "disposition_content_md"
DISPOSITION_CONTENT_BR = "disposition_content_br"
DISPOSITION_CONTENT_MDBR = "disposition_content_mdbr"
DISPOSITION_CONTENT_NONE = "disposition_content_none"

REL_ORIGINAL_DEPOSIT = "http://purl.org/net/sword/3.0/terms/originalDeposit"

DIGEST_SHA_256 = "SHA-256"
DIGEST_MD5 = "MD5"

URI_METADATA = "http://purl.org/net/sword/3.0/types/Metadata"

PACKAGE_BINARY = "http://purl.org/net/sword/3.0/package/Binary"
PACKAGE_SWORDBAGIT = "http://purl.org/net/sword/3.0/package/SWORDBagIt"
PACKAGE_SIMPLEZIP = "http://purl.org/net/sword/3.0/package/SimpleZip"

CREATED = 201
ACCEPTED = 202


class DocumentType:
    ServiceDocument = "ServiceDocument"
    Metadata = "Metadata"
    Status = ("Status",)
    ByReference = "ByReference"
    Temporary = "Temporary"


class DigestName:
    MD5 = "MD5"
    SHA256 = "SHA-256"


class MetadataFormat:
    Sword = "http://purl.org/net/sword/3.0/types/Metadata"


class PackagingFormat:
    Binary = "http://purl.org/net/sword/3.0/package/Binary"
    SwordBagIt = "http://purl.org/net/sword/3.0/package/SWORDBagIt"
    SimpleZip = "http://purl.org/net/sword/3.0/package/SimpleZip"


class Rel:
    FileSetFile = "http://purl.org/net/sword/3.0/terms/fileSetFile"
    OriginalDeposit = "http://purl.org/net/sword/3.0/terms/originalDeposit"
    DerivedResource = "http://purl.org/net/sword/3.0/terms/derivedResource"
    FormattedMetadata = "http://purl.org/net/sword/3.0/terms/formattedMetadata"
    ByReferenceDeposit = "http://purl.org/net/sword/3.0/terms/byReferenceDeposit"


class DepositState:
    InProgress = "http://purl.org/net/sword/3.0/state/inProgress"
    Ingested = "http://purl.org/net/sword/3.0/state/ingested"


class FileState:
    Ingested = "http://purl.org/net/sword/3.0/filestate/ingested"
    Pending = "http://purl.org/net/sword/3.0/filestate/pending"


class RequestContexts:
    ByReference = "ByReference"
    Temporary = "Temporary"
    Metadata = "Metadata"
    MetadataAndByReference = "MetadataAndByReference"
    SegmentInit = "SegmentInit"
