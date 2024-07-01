from taurius_installer.orchestrator.orchestrator import Orchestrator
from tests.generics import CommonTestCase


class TestConfigAppDataFolder(CommonTestCase):
    def setUp(self):
        self.test_appname = "TestAppName"
        self.orchestrator = Orchestrator(self.test_appname)

    def tearDown(self):
        self.orchestrator._appdata.clear(everything=True)

    def test_it_should_be_able_to_configure_appdata_on_first_installation(self):
        self.assertEqual(self.orchestrator.version, "0.0.1")

        self.assertDictEqual(
            self.orchestrator.settings,
            {"application": self.test_appname, "version": "0.0.1"},
        )

        self.assertFalse(self.orchestrator.must_be_install_new_version)
        self.assertTrue(self.orchestrator.settings_filepath.exists())
        self.assertTrue(self.orchestrator.settings_filepath.is_file())

    def test_it_should_be_able_to_identify_new_version(self):
        test_new_version = "0.0.2"
        self.orchestrator = Orchestrator(self.test_appname, test_new_version)

        self.assertTrue(self.orchestrator.must_be_install_new_version)
        self.assertEqual(self.orchestrator.version, test_new_version)
        self.assertDictEqual(
            self.orchestrator.settings,
            {"application": self.test_appname, "version": test_new_version},
        )
