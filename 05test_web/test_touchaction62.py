import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions


class TouchAction1:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 滑动到底部
    '''
        打开Chrome浏览器
        打开url：http：//www.baidu.com
        向搜索框中输入'selenium测试'
        通过TouchAction点击搜素框
        滑动到底部，点击下一页
        关闭Chrome
        :return
        '''

    def test_touchactions(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_reach = self.driver.find_element_by_id('su')
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_reach)
        action.perform()

if __name__ == "main":
    pytest.main('-v', '-s', "test_touchaction62.py")



