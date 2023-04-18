import unittest
from config.webdriver_setup import WebDriverSetup


class Close(unittest.TestCase):
    WebDriverSetup.driver.quit()