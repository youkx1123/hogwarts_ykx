from sel_frame_window7.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 如果操作frame的话需要切换到要操作的frame下
        self.driver.switch_to.frame("iframeResult")
        # 两种方式都可以，通常用上面的
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # 切换到默认页面，点击【点击运行】
        # 切换到当前父的frame节点
        # self.driver.switch_to.parent_frame()
        # 切换到默认的节点，即刚打开的链接
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id('submitBTN').text)


