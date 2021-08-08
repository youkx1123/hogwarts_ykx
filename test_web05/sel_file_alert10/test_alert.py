import self
from sel_js9.base import Base
from selenium.webdriver import ActionChains
from time import sleep

class TestAlert(Base):
    def test_alert(self):
        """
        1打开网页：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        2操作窗口右侧页面，将元素1拖拽到元素2
        3这是会有一个alert 弹框，点击弹框中国的“确定”
        4然后在点击“点击运行”
        5关闭网页
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        print("点击alert确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)









