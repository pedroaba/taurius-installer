import os
import shutil
from pathlib import Path

from taurius_installer.installer.installer import Installer
from tests.generics import CommonTestCase


class TestInstallExecutable(CommonTestCase):
    def setUp(self):
        self.main_executable_filename = "electron.vite.config.ts"
        self.basepath = Path(os.getcwd())
        self.executable_filepath = (
            self.basepath / "tests" / "files" / "rotion-0.0.3.zip"
        )
        self.executable_filename = f"{self.executable_filepath.stem} (test-installer){self.executable_filepath.suffix}"
        self.executable_filepath_copy = (
            self.basepath / "tests" / "files" / self.executable_filename
        )

        shutil.copy2(self.executable_filepath, self.executable_filepath_copy)

        self.installation_folder = self.basepath / "test-installation"
        self.installation_executable_filepath = (
            self.installation_folder / self.executable_filename
        )

        self.installer = Installer(
            self.executable_filepath_copy, self.installation_executable_filepath
        )

    def tearDown(self):
        if self.installation_folder.exists():
            shutil.rmtree(self.installation_folder)

    def test_it_should_be_able_to_install_executable_on_specified_folder(self):
        self.installer.install()
        executable_folder = (
            self.installation_folder / self.executable_filepath.stem
        )

        main_executable_filepath = (
            executable_folder / self.main_executable_filename
        )

        self.assertTrue(executable_folder.exists())
        self.assertTrue(main_executable_filepath.exists())
