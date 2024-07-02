import os
import importlib

import dotenv

from taurius_installer.exceptions import NoEntrypointFile


dotenv.load_dotenv()


class TauriusInstaller:
    def __init__(self, app_name: str):
        self._app_name = app_name
        self._config_module_import_name = os.getenv("CONFIG_MODULE_PACKAGE_IMPORT", "installer_config.py")

    def load_configs(self):
        self._import_config_dynamic()
        if not hasattr(self._config_module, "ENTRYPOINT"):
            raise NoEntrypointFile()

    def _import_config_dynamic(self):
        self._config_module = importlib.import_module(self._config_module_import_name)
