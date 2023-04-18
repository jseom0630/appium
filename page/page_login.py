from .page_base import PageBase
from locator.loc_login import LoginLocators
from appium.webdriver.common.appiumby import AppiumBy


class PageLogin(PageBase):
    btn_id = LoginLocators.BUTTON_ID
    txt_id = (LoginLocators.TEXT_ID)

    btn_pw = (LoginLocators.BUTTON_PASSWORD)
    txt_pw = (LoginLocators.TEXT_PW)

    btn_unitylogin = (LoginLocators.BUTTON_UNITYLOGIN)