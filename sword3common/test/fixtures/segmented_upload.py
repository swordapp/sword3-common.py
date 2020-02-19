from copy import deepcopy


class SegmentedUploadFixtureFactory(object):
    @classmethod
    def segmented_upload_status(
        self, received=None, expecting=None, size=None, segment_size=None
    ):
        status = deepcopy(SEGMENTED_UPLOAD_STATUS)

        received = received if received is not None else [1, 2, 3, 4, 5]
        expecting = expecting if expecting is not None else []
        size = size if size is not None else 10000000
        segment_size = segment_size if segment_size is not None else 2000000

        status["segments"]["received"] = received
        status["segments"]["expecting"] = expecting
        status["segments"]["size"] = size
        status["segments"]["segment_size"] = segment_size

        return status


SEGMENTED_UPLOAD_STATUS = {
    "@context": "https://swordapp.github.io/swordv3/swordv3.jsonld",
    "@id": "http://example.com/temporary/1",
    "@type": "Temporary",
    "segments": {
        "received": [],
        "expecting": [],
        "size": 10000000,
        "segment_size": 2000000,
    },
}
