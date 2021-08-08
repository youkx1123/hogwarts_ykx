# selenium执行js脚本
from time import sleep

from sel_js9.base import Base


class TestJs(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # 使用js定位元素document.getElementById("su") 需要返回值使用"return"
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(5)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(5)
        for code in {
            "return document.title", "return JSON.stringify(performance.timing)"
        }:
            print(self.driver.execute_script(code))
        sleep(5)

    # 使用js定位到出发日期，修改出发时间为2021年12月31日，打印出发时间
    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2021-12-31'")
        sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
        sleep(5)
