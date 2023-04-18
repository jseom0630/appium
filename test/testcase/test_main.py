import time
import unittest
from page.page_main import PageMain
from page.page_together import PageTogether
from test.testcase.test_start import TestAppLaunch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 기존 웹드라이버 사용 시 import > TestApplaunch.driver
# class TestClass(unittest.TestCase)
# class TestSplash(WebDriverSetup):

class TestMain(unittest.TestCase):
    def setUp(self):
        self.page = PageMain(TestAppLaunch.driver)
        self.page2 = PageTogether(TestAppLaunch.driver)

    #로고 노출 확인
    def test_00_logo_displayed(self):
        is_logo_visible = self.page.is_element_visible(self.page.btn_logo)  # self.page.btn
        assert is_logo_visible, "로고가 보이지 않습니다."

    #배너 클릭
    def test_01_banner_click(self):
        self.page.click(self.page.btn_banner)

    #배너 상세 > 뒤로가기 클릭
    def test_02_back_click(self):
        time.sleep(5)
        self.page2.click(self.page2.btn_back)

    #함께챌린지 배너 클릭
    def test_03_together_click(self):
        time.sleep(5)
        self.page.click(self.page.btn_together)

    #함께챌린지 상세 > 뒤로가기 클릭
    def test_04_back_click(self):
        time.sleep(5)
        self.page2.click(self.page2.btn_back)

    #함께챌린지 더보기 클릭
    def test_05_togethermore_click(self):
        time.sleep(5)
        self.page.click(self.page.btn_together)

    #함께챌린지 상세 > 뒤로가기 클릭
    def test_06_back_click(self):
        time.sleep(5)
        self.page2.click(self.page2.btn_back)

    #페이지 스크롤 > 안됨
    #def test_07_scroll(self, direction="up"):
    #    self.page.execute_script("window.scrollBy(0, -500);")

    #헌혈배너 클릭
    def test_07_continuous_click(self):
        time.sleep(5)
        self.page.click(self.page.btn_continuous)

   #헌혈배너 상세 > 뒤로가기 클릭
    def test_08_back_click(self):
        time.sleep(5)
        self.page2.click(self.page2.btn_back)

if __name__ == '__main__':
            unittest.main()