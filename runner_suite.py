import unittest
import HtmlTestRunner
from test.testsuite.test_suite_1 import TestSuite1

if __name__ == '__main__':
        # HTML Test Runner 설정
    runner = HtmlTestRunner.HTMLTestRunner(
        output='../test_result/',
        report_name='testsuite_report',
        report_title='All Tests Results'
      
        # combine_reports=True
    )
    suite = unittest.TestSuite()
    suite.addTests(TestSuite1())
    runner.run(suite)
    
    
    