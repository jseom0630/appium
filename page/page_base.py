from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class PageBase:
    """ 모든 페이지에서 공통으로 사용할 메서드를 정의한다 """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    # 엘리먼트 클릭
    def click(self, by_locator):        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # 엘리먼트에 키 입력
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # 화면 스크롤
    def scroll(self, direction):
        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0, -500);")
        elif direction == 'down':
            self.driver.execute_script("window.scrollBy(0, 500);")

    # 화면 스와이프
    def swipe(self, direction):
        size = self.driver.get_window_size()
        if direction == 'up':
            start_x = size['width'] / 2
            start_y = size['height'] * 0.8
            end_x = size['width'] / 2
            end_y = size['height'] * 0.2
        elif direction == 'down':
            start_x = size['width'] / 2
            start_y = size['height'] * 0.2
            end_x = size['width'] / 2
            end_y = size['height'] * 0.8
        elif direction == 'left':
            start_x = size['width'] * 0.8
            start_y = size['height'] / 2
            end_x = size['width'] * 0.2
            end_y = size['height'] / 2
        elif direction == 'right':
            start_x = size['width'] * 0.2
            start_y = size['height'] / 2
            end_x = size['width'] * 0.8
            end_y = size['height'] / 2

        self.driver.swipe(start_x, start_y, end_x, end_y)

    # 엘리먼트가 존재하는지 확인
    def is_element_present(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return True
        except:
            return False

    # 엘리먼트가 화면에 보이는지 확인
    def is_element_visible(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False
