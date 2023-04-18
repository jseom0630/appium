import unittest
from page.page_login import PageLogin
from test.testcase.test_start import TestAppLaunch


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.page = PageLogin(TestAppLaunch.driver)

    def test_send_id(self):
        self.page.send_keys(self.page.txt_id, 'hjtest43')

    def test_send_pw(self):
        self.page.send_keys(self.page.txt_pw, 'qwer1234!')

    def test_unitylogin_button_click(self):
        self.page.click(self.page.btn_unitylogin)

if __name__ == '__main__':
    unittest.main()
