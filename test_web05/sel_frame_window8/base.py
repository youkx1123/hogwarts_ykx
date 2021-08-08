import os

from selenium import webdriver


class Base:

    # selenium多浏览器处理
    def setup(self, webdriver):
        # 通过os.getenv()获取参数browser
        browser = os.getenv('browser')
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


