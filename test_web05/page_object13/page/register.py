from selenium.webdriver.common.by import By


class Register():

    def register(self):
        self.find(By.ID, "corp_name").send_keys("蜡笔小新")
        self.find(By.ID, "manager_name").send_keys("luna")
        return True
