import json
from pathlib import Path

from appdata import AppDataPaths

from taurius_installer.exceptions import NotFoundAVersionOnMachine, InvalidReleasePath
from taurius_installer.protocols.provider import Provider


class Orchestrator:
    def __init__(
            self,
            application_name: str,
            application_version: str = None,
    ):
        self.appdata_folder = AppDataPaths()

        # control variable
        self.__application_version = application_version
        self.__application_name = application_name

        # configs
        self.__config_content = {}

    def _setup(self):
        self.appdata_folder.setup()

        config_path = Path(self.appdata_folder.config_path)
        config_file_path = config_path / f"{self.__application_name}.json"
        if not config_path.exists():
            if self.__application_version is None:
                raise NotFoundAVersionOnMachine()

            config_path.mkdir(exist_ok=True)

            self.__config_content = {
                "version": self.__application_version,
                "name": self.__application_name,
            }

            config_file_path.write_text(
                json.dumps(self.__config_content)
            )
        else:
            with open(config_file_path, "rb") as f:
                self.__config_content = json.load(f)

    def check_for_updates_and_install(self, provider: Provider):
        has_new_updates = provider.check_by_updates()

        if not has_new_updates:
            return False

        new_version_path = provider.download_updates()
        if not new_version_path.exists():
            raise InvalidReleasePath()

        self._initialize_installation()

    def _initialize_installation(self):
        """Call other process to install it
        :return:
        """
        pass
