import os
import unittest
import HtmlTestRunner
# from Tests.TestCase.test_Splash import TestSplashScreen



if __name__ == '__main__':
    """테스트 케이스 디렉터리 전체 실행"""
    # 테스트케이스 디렉토리 경로
    testcase_dir = os.path.join(os.path.dirname(__file__), 'test', 'testcase')
        # discover 함수를 사용해서 테스트 케이스 로드
    suite = unittest.TestLoader().discover(testcase_dir)

    # HTML Test Runner 설정
    runner = HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name='all_tests_report',
        report_title='All Tests Results',
        combine_reports=False
    )
    
    

 
    # 테스트 실행
    runner.run(suite)
    
    """테스트 케이스 단일 실행"""
   # # Test Loader로 테스트 케이스 불러오기
    # test_loader = unittest.TestLoader()
    # test_names = test_loader.getTestCaseNames(TestSplashScreen)
    # suite = unittest.TestSuite()
    # for name in test_names:
    #     suite.addTest(TestSplashScreen(name))

    # # HTML Test Runner 설정
    # runner = HtmlTestRunner.HTMLTestRunner(
    #     output='reports',
    #     report_name='splash_screen_report',
    #     report_title='Splash Screen Test Results',
    #     combine_reports=False
    # )
