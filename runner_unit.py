import unittest
from test.testcase.test_start import TestAppLaunch
from test.testcase.test_splash import TestSplash

if __name__ == '__main__':
    loader = unittest.TestLoader()
    # suite = loader.loadTestsFromTestCase(TestAppLaunch)
    suite = loader.loadTestsFromTestCase(TestSplash)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
