import requests

from taurius_installer.types import FetchMethod, FetcherResponse
from taurius_installer.exceptions import InvalidFetchMethod


class Fetcher:
    def __init__(self, url_to_fetch_info: str):
        self._url_to_fetch_info = url_to_fetch_info

    @property
    def url(self):
        return self._url_to_fetch_info

    def _get_auth_header(self):
        return {}

    def fetch_application_info(self, method: FetchMethod) -> tuple[FetcherResponse, int]:
        auth_header = self._get_auth_header()

        match method:
            case FetchMethod.POST:
                app_info_response = requests.post(self._url_to_fetch_info, auth=auth_header, headers={
                    "Content-Type": "application/json"
                })
            case FetchMethod.GET:
                app_info_response = requests.get(self._url_to_fetch_info, auth=auth_header, headers={
                    "Content-Type": "application/json"
                })
            case _:
                raise InvalidFetchMethod(method)

        return app_info_response.json(), app_info_response.status_code
