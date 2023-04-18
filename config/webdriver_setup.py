from appium import webdriver    # appium.webdriver 임포트
import config       # config 모듈 임포트, desired_caps 환경변수
import unittest

class WebDriverSetup(unittest.TestCase):
    # def __init__(cls):
    #     cls.envconfig = config.EnvConfig()
    #     cls.deviceconfig = config.DeviceConfig()
    #     cls.appconfig = config.AppConfig()
    
    envconfig = config.EnvConfig()
    deviceconfig = config.DeviceConfig()
    appconfig = config.AppConfig()
    driver = None
    
    @classmethod 
    def setUpClass(cls):
    # Create Appium WebDriver
        desired_caps = {
            'platformName': cls.deviceconfig.PLATFORM_NAME,
            'platformVersion': cls.deviceconfig.PLATFORM_VERSION,
            'deviceName': cls.deviceconfig.DEVICE_NAME,
            'automationName': cls.deviceconfig.AUTOMATION_NAME,
            'appPackage': cls.appconfig.APP_PACKAGE,
            'appActivity': cls.appconfig.APP_ACTIVITY
            # 'noReset': config.NO_RESET # noReset 설정이 필요한 경우 주석 해제
        }
        appium_url = f"http://{cls.envconfig.SERVER_IP}:{cls.envconfig.SERVER_PORT}/wd/hub"
        cls.driver = webdriver.Remote(appium_url, desired_caps)
            
    @classmethod      
    def tearDownClass(cls):        
        pass
            
if __name__ == '__main__':
    unittest.main()
    
# class WebDriverSetup:
#     # 앱이 실행되었는지 여부를 저장하는 클래스 변수
#     is_app_started = False
    
#     @classmethod
#     def setUpClass(cls):
#         if not cls.is_app_started:
#             # Create Appium WebDriver
#             desired_caps = {
#                 'platformName': cls.deviceconfig.PLATFORM_NAME,
#                 'platformVersion': cls.deviceconfig.PLATFORM_VERSION,
#                 'deviceName': cls.deviceconfig.DEVICE_NAME,
#                 'automationName': cls.deviceconfig.AUTOMATION_NAME,
#                 'appPackage': cls.appconfig.APP_PACKAGE,
#                 'appActivity': cls.appconfig.APP_ACTIVITY,
#                 # 'noReset': config.NO_RESET # noReset 설정이 필요한 경우 주석 해제
#             }
#             appium_url = f"http://{cls.envconfig.SERVER_IP}:{cls.envconfig.SERVER_PORT}/wd/hub"
#             cls.driver = webdriver.Remote(appium_url, desired_caps)
#             # 앱이 실행되었음을 표시
#             cls.is_app_started = True
    
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
        

        
        
        
        
        
        
        
        
        
    # @classmethod
    #     # 클래스 메서드임을 나타내는 파이썬 데코레이터
    #     # 데코레이터를 사용하여 정의된 메서드는 인스턴스가 아닌 클래스에 바인딩 됨
    #     # 클래스 메서드는 인스턴스에서 호출하는 것이 아니라 클래스에서 직접 호출됨(인스턴스 생성하지 않고 해당 메서드 사용 가능)
    #     # 클래스 변수를 다루거나, 클래스 수준에서 작업을 수행
    #     # 클래스 메서드보다는 테스트 코드와 웹드라이버 초기화 코드를 분리하여 작성하는게 권장됨
        
    # def setUpClass(cls):
    #     # Create Appium WebDriver
    #     # 모든 테스트케이스가 실행될 때마다 setUpClass()와 tearDownClass() 메서드를 실행
    #     # 각각 테스트 케이스마다 setUp()과, tearDown() 메서드를 실행
    #     # cls > 현재 클래스를 메서드의 매개변수로하여 인스턴스 생성 없이 초기화 및 클래스 변수에 접근
    #     desired_caps = {
    #         'platformName': config.PLATFORM_NAME,
    #         'platformVersion': config.PLATFORM_VERSION,
    #         'deviceName': config.DEVICE_NAME,
    #         'automationName': config.AUTOMATION_NAME,
    #         'appPackage': config.APP_PACKAGE,
    #         'appActivity': config.APP_ACTIVITY,
    #         # 'noReset': config.NO_RESET # noReset 설정이 필요한 경우 주석 해제
    #     }
    #     appium_url = f"http://{config.SERVER_IP}:{config.SERVER_PORT}/wd/hub"
    #     cls.driver = webdriver.Remote(appium_url, desired_caps)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
        

        


# class WebDriverSetup(unittest.TestCase):
#     def __init__(cls):
#         cls.envconfig = config.EnvConfig()
#         cls.deviceconfig = config.DeviceConfig()
#         cls.appconfig = config.AppConfig()
        
#     @classmethod    
#     def setUpClass(cls):
#         # Create Appium WebDriver
#         desired_caps = {
#             'platformName': cls.deviceconfig.PLATFORM_NAME,
#             'platformVersion': cls.deviceconfig.PLATFORM_VERSION,
#             'deviceName': cls.deviceconfig.DEVICE_NAME,
#             'automationName': cls.deviceconfig.AUTOMATION_NAME,
#             'appPackage': cls.appconfig.APP_PACKAGE,
#             'appActivity': cls.appconfig.APP_ACTIVITY,
#             # 'noReset': config.NO_RESET # noReset 설정이 필요한 경우 주석 해제
#         }
#         appium_url = f"http://{config.SERVER_IP}:{config.SERVER_PORT}/wd/hub"
#         cls.driver = webdriver.Remote(appium_url, desired_caps)
        
#     @classmethod
#     def tearDown(cls):
#         cls.driver.quit()