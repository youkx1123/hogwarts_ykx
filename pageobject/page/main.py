from atexit import register

from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage
from pageobject.page.login import Login
from pageobject.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return register(self._driver)

    def got_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
