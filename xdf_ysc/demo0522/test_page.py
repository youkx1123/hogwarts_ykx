from time import sleep

from selenium import webdriver


class TestPage:
    driver = None

    def login(self, url, username, password):
        # 浏览器
        self.driver = webdriver.Chrome()
        # 获取地址
        self.driver.get(url)
        # 用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys(username)
        # 密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys(password)
        # 等待时间内手动输入验证码
        sleep(10)
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/button').click()
        sleep(2)

    def member_list(self):
        # 点击用户管理
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/div/div/span').click()
        sleep(3)
        # 点击员工列表
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/ul/li[1]/span').click()
        # 获取默认的员工列表数据
        member_list1 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
        sleep(2)

        for i in range(len(member_list1)):
            # 取默认的列表中姓名
            member_name1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+']/td[2]/div').text
            # 取默认的列表中手机号
            member_mobile1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+']/td[3]/div').text
            # 输入姓名搜索
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[1]/div/input').send_keys(member_name1)
            # 点击搜索按钮
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[1]').click()
            sleep(2)
            # 获取搜索后的列表数据
            member_list2 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
            sleep(2)

            for j in range(len(member_list2)):
                # 获取查询后的列表中的手机号码
                member_mobile2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(j+1)+']/td[3]/div').text
                # member_mobile2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[3]/div').text
                sleep(2)

                if member_mobile1 == member_mobile2:
                    print("员工姓民:{}, 手机号码：{} 等于 手机号：{}".format(member_name1, member_mobile1, member_mobile2))
                else:
                    print("员工姓民:{}, 手机号码：{} 不等于 手机号：{}".format(member_name1, member_mobile1, member_mobile2))

            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[2]/span').click()
            sleep(2)

    def quit(self):
        self.driver.quit()




















