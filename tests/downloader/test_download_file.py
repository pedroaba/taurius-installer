from pathlib import Path

from taurius_installer.downloader.downloader import Downloader
from tests.generics import CommonTestCase


class TestDownloadFile(CommonTestCase):
    test_folder_name = "test-folder"

    def setUp(self):
        self.test_filename = "TestDownload"
        self.test_url = (
            "https://firebasestorage.googleapis.com/v0/b/inspetor-database-eb605.appspot.com/o/rotion-0.0"
            ".3.zip?alt=media&token=47c083f4-6a93-4a0f-b99d-eaed026c578b"
        )
        self.downloader = Downloader(self.test_filename)

        self.path_to_exclude: Path

    def tearDown(self):
        if hasattr(self, "path_to_exclude"):
            self.path_to_exclude.unlink(missing_ok=True)

        try:
            test_folder = Path(self.test_folder_name)
            if test_folder.exists():
                test_folder.rmdir()
        except Exception as e:
            print(e)

    def test_download_file(self):
        self.downloader.download_from(self.test_url)
        expected_downloaded_path = Path(
            f"{self.test_filename}.{self.downloader.DOWNLOAD_FILE_TYPE}"
        )

        self.assertTrue(expected_downloaded_path.exists())

        self.path_to_exclude = expected_downloaded_path

    def test_download_file_to_specific_path(self):
        path_to_save_file = Path(self.test_folder_name)

        self.downloader.set_path_to_download(path_to_save_file)
        self.downloader.download_from(self.test_url)
        path_to_save_file /= (
            f"{self.test_filename}.{self.downloader.DOWNLOAD_FILE_TYPE}"
        )

        self.assertTrue(path_to_save_file.exists())

        self.assertEqual(self.downloader.path, path_to_save_file)
        self.assertTrue(self.downloader.path.samefile(path_to_save_file))

        self.path_to_exclude = path_to_save_file
