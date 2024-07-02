from enum import Enum
from typing import TypedDict


class FetchMethod(Enum):
    POST = "POST"
    GET = "GET"


class FetcherResponse[ExtraInfoType](TypedDict):
    application_name: str
    download_url: str
    version: str
    extra_info: ExtraInfoType
