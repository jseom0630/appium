from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy


class SplashLocators:
    BUTTON_START = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button/android.widget.TextView")
    # BUTTON_START = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button/android.widget.TextView")
    # By, AppiumBy 상관없음. import만 잘해주면 됨
    BUTTON_START_CLASS = (By.CLASS_NAME, "android.widget.Button")
    BUTTON_START_TEXT = (By.LINK_TEXT, "시작하기")

    BUTTON_LOGIN = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button/android.widget.TextView")
    BUTTON_LOGIN_CLASS = (By.CLASS_NAME, "android.widget.Button")
    BUTTON_LOGIN_TEXT = (By.LINK_TEXT, "로그인 하기")
# 테스트
