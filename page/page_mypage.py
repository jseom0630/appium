from .page_base import PageBase
from locator.loc_mypage import MypageLocators
from appium.webdriver.common.appiumby import AppiumBy


class PageMypage(PageBase):
    btn_mypage = MypageLocators.BUTTON_MYPAGE
    btn_setting = MypageLocators.BUTTON_SETTING
    btn_logout = MypageLocators.BUTTON_LOGOUT
    btn_logoutok = MypageLocators.BUTTON_LOGOUTOK