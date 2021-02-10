import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDome1:

    def setup_method(self):
        print(1)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def teardown_method(self):
        time.sleep(3)
        self.driver.quit()
        print("it is closed")

    def test_dome1(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1440, 900)
        self.driver.find_element(By.XPATH, '//*[@id="ember5"]/header/div/div/div[2]/span/button[1]/span').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-link"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="login-account-name"]').send_keys("996190188@qq.com")
        self.driver.find_element(By.XPATH, "//*[@id='login-account-password']").send_keys("you@881123")
        self.driver.find_element(By.XPATH, "//*[@id='login-button']/span").click()