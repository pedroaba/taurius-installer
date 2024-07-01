import json
from pathlib import Path

from appdata import AppDataPaths


class Orchestrator:
    def __init__(
        self, application_name: str, application_version: str = "0.0.1"
    ):
        self._application_name = application_name
        self._version = application_version

        self._config_filename = "settings.json"

        self._appdata = AppDataPaths(application_name)
        self._lock_path = Path(self._appdata.locks_path)

        self._settings = {
            "application": self._application_name,
            "version": self._version,
        }

        self._must_be_install_new_version = False

        self._setup_of_appdata()
        self._load_configs()

    @property
    def must_be_install_new_version(self):
        return self._must_be_install_new_version

    @property
    def settings(self):
        return self._settings

    @property
    def name(self):
        return self._application_name

    @property
    def version(self):
        return self._version

    @property
    def settings_filepath(self):
        return self._lock_path / self._config_filename

    def _setup_of_appdata(self):
        self._appdata.setup()

    def _set_on_settings_on_config_file(self, settings_filepath: Path):
        with open(settings_filepath, "w") as configs:
            json.dump(self._settings, configs)

    def _set_new_version_on_config_file(
        self, settings_path: Path, new_version: str
    ):
        self._settings["version"] = new_version
        self._set_on_settings_on_config_file(settings_path)

    def _load_configs(self):
        has_already_installed_before = False
        settings_filepath = self._lock_path / self._config_filename
        if not settings_filepath.exists():
            self._set_on_settings_on_config_file(settings_filepath)
        else:
            has_already_installed_before = True
            with open(settings_filepath, "r") as configs:
                self._settings = json.load(configs)

        if has_already_installed_before:
            has_new_version_to_install = self._check_if_has_new_version()
            if has_new_version_to_install:
                self._set_new_version_on_config_file(
                    settings_filepath, self._version
                )

            self._must_be_install_new_version = has_new_version_to_install

    def _check_if_has_new_version(self) -> bool:
        (
            possible_new_major_version,
            possible_new_minor_version,
            possible_new_patch_version,
        ) = list(map(int, self._version.split(".")))

        old_major_version, old_minor_version, old_patch_version = list(
            map(int, self._settings["version"].split("."))
        )

        if possible_new_major_version > old_major_version:
            return True
        elif possible_new_minor_version > old_minor_version:
            return True
        elif possible_new_patch_version > old_patch_version:
            return True

        return False
