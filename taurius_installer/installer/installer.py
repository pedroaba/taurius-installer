import shutil
import zipfile
from pathlib import Path


class Installer:
    def __init__(self, filepath: Path, destiny_installation: Path):
        if not filepath.exists():
            raise FileNotFoundError(filepath)

        if not destiny_installation.exists():
            destiny_installation.parent.mkdir(parents=True, exist_ok=True)

        self._origin = filepath
        self._destiny = destiny_installation

        self._setup_folders()

    def set_origin_filepath(self, filepath: Path):
        if not filepath.exists():
            raise FileNotFoundError(filepath)

        self._origin = filepath

    def set_destity_filepath(self, filepath: Path):
        if not filepath.exists():
            filepath.parent.mkdir(parents=True, exist_ok=True)

        self._destiny = filepath

    def _setup_folders(self):
        self._origin_folder = self._origin.parent.absolute()
        self._destiny_folder = self._destiny.parent.absolute()

    def _move_file_to_installation_path(self):
        shutil.copy2(self._origin, self._destiny)

    def _clear_installation(self):
        self._origin.unlink()
        self._destiny.unlink()

    def install(self):
        self._move_file_to_installation_path()

        with zipfile.ZipFile(self._origin, "r") as executable:
            executable.extractall(self._destiny_folder)

        self._clear_installation()
