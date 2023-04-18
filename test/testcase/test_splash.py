import time
import unittest
from page.page_splash import PageSplash



# 기존 웹드라이버 사용 시 import > TestApplaunch.driver
# class TestClass(unittest.TestCase)
# class TestSplash(WebDriverSetup):

import unittest
from config.webdriver_setup import WebDriverSetup





class TestSplash(WebDriverSetup):
    def setUp(self):
        self.page = PageSplash(WebDriverSetup.driver)

    def test_00_start_displayed(self):
        is_start_button_visible = self.page.is_element_visible(self.page.btn_start)  # self.page.btn
        assert is_start_button_visible, "시작하기 버튼이 보이지 않습니다."

    def test_01_start_button_click(self):
        self.page.click(self.page.btn_start)

    def test_02_login_displayed(self):  # test_ < 붙여야 TC로 인식됨
        is_login_displayed = self.page.is_element_visible(PageSplash.btn_login)
        assert is_login_displayed, "Login button not displayed after clicking Start button"

    def test_03_login_button_click(self):
        time.sleep(5)
        self.page.click(PageSplash.btn_login)



