from time import sleep
from sel_frame_window7.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        # 打印当前窗口的
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        # 打印当前窗口的
        print(self.driver.current_window_handle)
        # 打印所有的窗口
        print(self.driver.window_handles)
        window = self.driver.window_handles
        # window是一个列表，选取列表的最后一位，即最后一个窗口立即注册窗口
        self.driver.switch_to.window(window[-1])
        # self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("userName222")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("18510929499")
        sleep(5)
        self.driver.switch_to.window(window[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("18510929499")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("you@881123")
        sleep(5)
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(15)




