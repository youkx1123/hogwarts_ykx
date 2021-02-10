from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com.cn")

    def teardown(self):
        sleep(8)
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃滋学院")
        # 多种方式定位元素
        # self.driver.find_element(By.ID, "su").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#su").click()
        # self.driver.find_element_by_id('su')
        self.driver.find_element(By.CSS_SELECTOR, '[id=su]').click()



