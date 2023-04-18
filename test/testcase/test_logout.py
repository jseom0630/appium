import unittest
from page.page_mypage import PageMypage
from test.testcase.test_start import TestAppLaunch

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.page = PageMypage(TestAppLaunch.driver)

    def test_01_mypage_button_click(self):
        self.page.click(self.page.btn_mypage)

    def test_02_setting_button_click(self):
        self.page.click(self.page.btn_setting)

    def test_03_logout_button_click(self):
        self.page.click(self.page.btn_logout)

    def test_04_logoutok_button_click(self):
        self.page.click(self.page.btn_logoutok)

if __name__ == '__main__':
    unittest.main()
