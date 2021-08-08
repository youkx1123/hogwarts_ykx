import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium1:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(3)

    def teardown(self):
        time.sleep(10)
        self.driver.quit()

    def test_SR(self):
        # self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "kw").send_keys("高考分数线")
        self.driver.find_element(By.ID, "su").click()
