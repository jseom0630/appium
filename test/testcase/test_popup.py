import unittest
import time
from page.page_main import PageMain
from test.testcase.test_start import TestAppLaunch
    # 기존 웹드라이버 사용 시 import > TestApplaunch.driver
    # class TestClass(unittest.TestCase)
    # class TestSplash(WebDriverSetup):

class TestPopup(unittest.TestCase):

    def setUp(self):
        self.page = PageMain(TestAppLaunch.driver)

    def test_01_ok_button_click(self):
        time.sleep(5)
        self.page.click(self.page.btn_ok)


    # 마케팅 수신 동의 > 동의 클릭
    def test_02_mkagree_button_click(self):
        time.sleep(5)
        self.page.click(self.page.btn_mkagree)

   # 메인 팝업 배너 닫기
    def test_03_popupclose_button_click(self):
        time.sleep(5)
        self.page.click(self.page.btn_close)

if __name__ == '__main__':
    unittest.main()