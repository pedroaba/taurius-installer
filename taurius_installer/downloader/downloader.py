import os
from pathlib import Path

import requests


class Downloader:
    DOWNLOAD_FILE_TYPE = "zip"

    def __init__(self, filename):
        self._path_to_save_file = Path(os.getcwd())
        self._filename = filename

    def set_path_to_download(self, download_path: Path):
        if not download_path.exists():
            download_path.mkdir(parents=True, exist_ok=True)

        self._path_to_save_file = download_path

    def download_from(self, url: str):
        auth_header = self._get_auth_header()

        response = requests.get(url, auth=auth_header, stream=True)
        with open(self.path, "wb") as executable_file:
            for chunk in response.iter_content(chunk_size=10 * 1024):
                executable_file.write(chunk)

        print("The executable has been downloaded.")

    def _get_auth_header(self):
        """This function returns a basic authentication header"""
        return {}

    @property
    def path(self) -> Path:
        return (
            self._path_to_save_file
            / f"{self._filename}.{self.DOWNLOAD_FILE_TYPE}"
        )
