from .page_base import PageBase
from locator.loc_splash import SplashLocators
from appium.webdriver.common.appiumby import AppiumBy


class PageSplash(PageBase):        
    
    
    btn_start = (SplashLocators.BUTTON_START)                   
    btn_login = (SplashLocators.BUTTON_LOGIN)
    
    # btn_positive = (AppiumBy.XPATH, SplashLocators.BUTTON_START) << 안됨    
    # btn_positive = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button/android.widget.TextView")               
    # btn_positive_class = (AppiumBy.CLASS_NAME, SplashLocators.BUTTON_START_CLASS)
    # btn_positive_text = (AppiumBy.LINK_TEXT, SplashLocators.BUTTON_START_TEXT)
    
    
    # def __init__(self, driver):
    #     """클래스의 생성자 / 객체가 생성될 때 자동으로 호출되는 메서드"""
    #     self.driver = driver
    #     self.wait = WebDriverWait(self.driver, 10)

    # def click_start_button(self):
    #     """시작하기 버튼 클릭"""
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, splashLocators.BUTTON_START))).click()

    # def click_login_button(self):
    #     """로그인 하기 버튼 클릭"""
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, splashLocators.BUTTON_LOGIN))).click()

    # def is_start_button_displayed(self):
    #     """시작하기 버튼이 표시되었는지 확인"""
    #     element = self.driver.find_element(By.XPATH, splashLocators.BUTTON_START)
    #     return element.is_displayed()


    # def is_login_button_displayed(self):
    #     """로그인 버튼이 로드될 때까지 대기"""
    #     login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, splashLocators.BUTTON_LOGIN)))
    #     return login_button.text == '로그인 하기'
