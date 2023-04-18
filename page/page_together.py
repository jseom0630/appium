from .page_base import PageBase
from locator.loc_together import TogetherLocators
from appium.webdriver.common.appiumby import AppiumBy


class PageTogether(PageBase):
    btn_back = (TogetherLocators.BUTTON_BACK)