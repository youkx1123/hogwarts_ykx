from time import sleep


from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChains:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(20)
        # self.driver.maximize_window()

    def teardown(self):
        sleep(2)
        self.driver.quit()

    # 不执行的测试用例

    # 鼠标点击
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # 单击、双击、右击
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    # 鼠标移动
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com.cn")
        ele = self.driver.find_element_by_id('s-usersetting-top')
        # ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self. driver)
        action.move_to_element(ele)
        sleep(3)
        action.perform()
        sleep(3)

    # 拖拽一个元素拖拽到另一个上面释放
    '''
    拖拽一个元素拖拽到另一个上面释放
    drag_and_drop(self,source,target) 调用两个参数，
    第一个参数source是"self.click_and_hold(source) 需要点击按并且按住不放
    第二个参数target是"release(target)释放
    '''
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action =ActionChains(self.driver)
        # 以下三种方法都可以
        # action.drag_and_drop(drag_element,drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    # 模拟按键方法
    # 定位输入框，点击输入空获取光标，输入"username"+"空格"+tom，然后删除"m"
    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        '''
        def send_keys(self,*keys_to_send):
        send_keys方法需要我们传入"*keys_to_send"参数，这个参数是我们要发给键盘的一个指令，调用keys模块
        keys模块中可以模拟各种操作，例如：TAB，null、BACKSPACE等，手机指令，手机键盘，实现f1到f12的操作，模拟键盘指令
        '''
        action.send_keys('username')
        # 调用send_keys里面的空格Keys.SPACE
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(20)

    def test_touchaction(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_reach = self.driver.find_element_by_id('su')
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_reach)
        action.perform()
        action.scroll_from_element(el, 0, 10000).perform()
        sleep(5)


if __name__ == "main":
    pytest.main('-v', '-s', "test_actionchains61.py")
