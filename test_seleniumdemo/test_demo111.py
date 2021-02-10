from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Selenium IDE 录制代码
1代码冗余
2还需要写断言
'''


class TestDome1:

    def setup_method(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        # 指定路径 webdriver.Chrome(executable_path="")
        self.driver = webdriver.Chrome(options=option)
        # 隐式等待，实例化driver后加，存在driver的整个生命周期中
        self.driver.implicitly_wait(2)

    def teardown_method(self):
        self.driver.quit()

    def test_dome1(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1440, 900)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        class1 = self.driver.find_element(By.LINK_TEXT, "所有分类").get_attribute("class")
        # 断言
        assert class1 == "active"
