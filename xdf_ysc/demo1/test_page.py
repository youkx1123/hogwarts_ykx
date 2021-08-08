from time import sleep

from selenium import webdriver


class TestWebPage:
    driver = None
    def login(self, url, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        sleep(3)
        # 用户名,密码，登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys(password)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/button/span').click()
        sleep(3)
    def member_list(self):
        # 点击用户管理
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/div/div/span').click()
        sleep(3)
        # 点击用户列表
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/ul/li[1]/span').click()
        sleep(3)
        # 输入姓名筛选
        a = "尤晓影"
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[1]/div/input').send_keys(a)
        # 点击搜索
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[1]/span').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[1]').click()
        sleep(6)
        # 展示搜索结果
        mobile1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div').text
        # mobile2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[3]/div').text

        name1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div').text
        # name2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div').text

        print("第一列表，姓名和电话是",  name1, mobile1,)
        # print("第二列表，姓名和电话是", name2, mobile2,)
        # 定位列表数据（搜索结果的全部数据）
        list1 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
        print("我是list1", list1)
        # 搜索结果条数
        count1 = len(list1)
        print(count1)
        for i in range(count1):
            name = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+"]/td[2]/div").text
            mobile = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+"]/td[3]/div").text
            print('第{}列:{}+{}'.format(i+1, name, mobile))
        for j in list1:
            l = j.text
            print(l)
        if a == name1:
            print("ture")
        else:
            print("flase")







    def quit(self):
        self.driver.quit()

















