from tests.generics import CommonTestCase
from taurius_installer.fetcher.fetcher import Fetcher
from taurius_installer.types import FetchMethod


class TestFetchApplicationInfoFromCloud(CommonTestCase):
    def setUp(self):
        self.test_url = ""

        self.fetcher = Fetcher(self.test_url)

    def test_it_should_be_able_to_get_the_app_info(self):
        response, status = self.fetcher.fetch_application_info(FetchMethod.POST)

        self.assertEqual(status, 200)
        self.assertDictContainsSubset(response, {
            "application_name": "",
            "version": "",
            "download_url": ""
        })

    def test_it_should_be_able_to_get_the_app_info_with_extra_information(self):
        response, status = self.fetcher.fetch_application_info(FetchMethod.POST)

        self.assertEqual(status, 200)
        self.assertDictContainsSubset(response, {
            "application_name": "",
            "version": "",
            "download_url": "",
            "extra_info": ""
        })
