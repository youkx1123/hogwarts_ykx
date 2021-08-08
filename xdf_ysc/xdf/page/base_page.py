from time import sleep

from selenium import webdriver


class Base_page:
    driver = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://test-staff.xdfgk.cn/login")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tear_down(self):
        sleep(3)
        self.driver.quit()





