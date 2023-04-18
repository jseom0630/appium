from .page_base import PageBase
from locator.loc_main import MainLocators
from appium.webdriver.common.appiumby import AppiumBy


class PageMain(PageBase):
    btn_ok = MainLocators.BUTTON_OK
    btn_mkagree = MainLocators.BUTTON_MKAGREE
    btn_mkdisagree = MainLocators.BUTTON_MKDISAGREE
    btn_close = MainLocators.BUTTON_POPUPCLOSE
    btn_logo = MainLocators.BUTTON_LOGO
    btn_banner = MainLocators.BUTTON_BANNER
    btn_together = MainLocators.BUTTON_TOGETHER
    btn_tgmore = MainLocators.BUTTON_TOGETHERMORE
    btn_continuous = MainLocators.BUTTON_CONTINUOUS