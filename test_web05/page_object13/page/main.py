from selenium.webdriver.common.by import By


from test_web05.page_object13.page.base_page import BasePage
from test_web05.page_object13.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def go_to_register(self):
        self.find(By.CSS.SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)



    def go_to_login(self):
        pass
