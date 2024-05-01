import pathlib
from typing import Protocol


class Provider(Protocol):
    def check_by_updates(self) -> bool:
        pass

    def download_updates(self) -> pathlib.Path:
        pass
