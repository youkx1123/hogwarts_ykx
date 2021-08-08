import time

from selenium import webdriver


class TestPage:
    driver = None
    def login(self, url, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys(password)
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/button').click()
        time.sleep(2)
    def member_list(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/div/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/ul/li[1]').click()
        list1 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
        for i in range(len(list1)):
            name1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(1)+']/td[2]/div').text
            mobile1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(1)+']/td[3]/div').text
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[1]/div/input').send_keys(name1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[1]/span').click()
            time.sleep(2)
            list2 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
            for j in list2:
                # mobile2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/tb[2]/div[0]').text
                mobile2 = j.find_element_by_xpath('td[3]').text
                if mobile1 == mobile2:
                    print("搜索{}，手机号{}与{}一致".format(name1, mobile1, mobile2))
                else:
                    print("搜索{}，手机号{}与{}不相同".format(name1, mobile1, mobile2))
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[2]/span').click()
                time.sleep(2)
    def quit(self):
        self.driver.quit()












