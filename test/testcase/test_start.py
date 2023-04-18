
import unittest
from config.webdriver_setup import WebDriverSetup


class TestAppLaunch(WebDriverSetup):
    def test_start(self):
        # Check that app is launched
        is_app_launched = self.driver.is_app_installed("com.marvrus.whosmvp")
        assert is_app_launched, "앱이 실행되지 않았습니다."

