import time
from selenium import webdriver


class TestPage:
    driver = None

    def longin_page(self, url, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys(password)
        time.sleep(8)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/button').click()
        time.sleep(3)
    def member_list_page(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/div/div/span').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/ul/li[1]/span').click()
        time.sleep(3)
        list1 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
        time.sleep(2)
        for i in range(len(list1)):
            name1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+']/td[2]/div').text
            mobile1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+']/td[3]/div').text
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[1]/div/input').send_keys(name1)
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[1]/span').click()
            time.sleep(2)
            list2 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
            time.sleep(3)
            for j in range(len(list2)):
                mobile2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(j+1)+']/td[3]/div').text
                if mobile1 == mobile2:
                    print("name{},手机号{}={}".format(name1, mobile1, mobile2))
                else:
                    print("name{},手机号{}不等于{}".format(name1, mobile1, mobile2))
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[2]/span').click()
                time.sleep(3)

    def quit(self):
        quit()








        self.driver.find_element_by_xpath()
        self.driver.find_element_by_xpath()
        self.driver.find_element_by_xpath()
        self.driver.find_element_by_xpath()








