import dataclasses
import sys
import inspect

from abc import ABC
from pathlib import Path

from examples.password_manager.src.utils.networks import find_available_port


class PathsManager(ABC):
    BASE_DIR: Path = None
    FLASK_SESSION_FOLDER: Path = None
    TEMPLATE_FOLDER: Path = None
    STATIC_FOLDER: Path = None

    def __init__(self):
        raise NotImplementedError()

    @staticmethod
    def setup_folders():
        PathsManager.BASE_DIR = Path(__file__).parent

        has_exe_envirment = getattr(sys, "frozen", False)  # PyInstaller environment
        if has_exe_envirment:
            meipass_folder = getattr(sys, "_MEIPASS", PathsManager.BASE_DIR)
        else:
            meipass_folder = PathsManager.BASE_DIR

        PathsManager.STATIC_FOLDER = PathsManager.BASE_DIR / "static"
        PathsManager.TEMPLATE_FOLDER = PathsManager.BASE_DIR / "templates"

        PathsManager.FLASK_SESSION_FOLDER = Path(meipass_folder) / "sessions"

        PathsManager._mount_folders()

    @staticmethod
    def _mount_folders():
        folders = PathsManager.__get_all_registry_paths()

        for folder in folders:
            path_to_create = getattr(PathsManager, folder, None)
            if path_to_create is not None and not path_to_create.exists():
                path_to_create.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def __get_all_registry_paths() -> list[str]:
        folders = []
        ignore_attributes = ["DEFAULT_MEIPASS_VALUE"]
        for name, value in inspect.getmembers_static(PathsManager):
            if not callable(value) and not name.startswith("_") and name not in ignore_attributes:
                folders.append(name)

        return folders


PathsManager.setup_folders()


@dataclasses.dataclass
class Config:
    FLASK_DEBUG = 1
    SESSION_FILE_DIR = PathsManager.FLASK_SESSION_FOLDER.absolute()
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SECRET_KEY = "k\x8d-\xbd\xb9\x05\xeax\x92\xd9{H\xf0\x9c\xf9\xde\x91\xc6\xe6\xa8\x14\xf9\x89t"


@dataclasses.dataclass
class ServerConfig:
    TEMPLATE_FOLDER = PathsManager.TEMPLATE_FOLDER.absolute()
    STATIC_FOLDER = PathsManager.STATIC_FOLDER.absolute()

    PORT = find_available_port()
    HOST = "127.0.0.1"
