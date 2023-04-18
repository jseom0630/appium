import unittest
from config.webdriver_setup import WebDriverSetup
from page.page_base import PageBase
from page.page_splash import PageSplash


class TestSplash2(WebDriverSetup):

    # @classmethod
    # def setUpClass(cls):
            
    #     # Create WebDriver
    #     cls.web_driver_setup = WebDriverSetup()
    #     cls.web_driver_setup.setUp()
    #     cls.driver = cls.web_driver_setup.driver
        
    # @classmethod
    # def tearDownClass(cls):
    #     # Quit WebDriver
    #     # cls.web_driver_setup.tearDown()
    #     pass
    

    def test_login_button_click(self):
        splash = PageSplash(self.driver)
        splash.click(PageSplash.btn_login)
        

        
        # splash.click(PageSplash.btn_positive_text)
        # splash.click_start_button()
        # is_login_displayed = splash.is_login_button_displayed()
        # assert splash.is_login_button_displayed(), "Login button not displayed after clicking Start button"



# # 클래스 메서드 사용 시
# class TestSplashScreen(WebDriverSetup):

#     def test_start_button_click(self):
#         splash = PageSplash(self.driver)
#         splash.click_start_button()
#         time.sleep(3)
#         assert splash.is_login_button_displayed() == True




# if __name__ == '__main__': 코드는 현재 스크립트가 메인 프로그램으로 실행될 때에만 unittest를 실행하도록 하는 역할
# 이 코드를 추가하지 않으면, 현재 스크립트가 모듈로서 다른 스크립트에서 import될 때에도 unittest가 실행되기 때문에
# 의도하지 않은 테스트가 실행될 수 있음
if __name__ == '__main__':
    unittest.main()
