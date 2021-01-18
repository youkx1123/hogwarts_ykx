from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage


class Register(BasePage):

    @property
    def Register(self):
        self.find(By.ID, "corp_name").send_keys("hello1")
        self.find(By.ID, "manager_name").send_keys("hello2")
        return True
