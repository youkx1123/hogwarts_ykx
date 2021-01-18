from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDome1:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_dome1(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1440, 900)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
