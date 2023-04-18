import unittest
from test.testcase.test_splash import TestSplash
from test.testcase.test_start import TestAppLaunch
# from test.testcase.test_login import TestLogin
from test.testcase.test_popup import TestPopup
# from test.testcase.test_logout import TestLogout
from test.testcase.test_main import TestMain

class TestSuite1(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTest(unittest.makeSuite(TestAppLaunch))
        self.addTest(unittest.makeSuite(TestSplash))
      # self.addTest(unittest.makeSuite(TestLogin))
        self.addTest(unittest.makeSuite(TestPopup))
        self.addTest(unittest.makeSuite(TestMain))
      #  self.addTest(unittest.makeSuite(TestLogout))