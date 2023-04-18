import unittest
from test.testcase.test_login import TestLogin

class TestSuite2(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTest(unittest.makeSuite(TestLogin))



