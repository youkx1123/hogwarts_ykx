from time import sleep

from selenium import webdriver


class TestWebPage1:
    driver = None

    def login(self, url, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys(password)
        sleep(10)
        # code1 = self.driver.find_element_by_xpath('//*[@id="canvas"]').text
        # sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/div/div/input').send_keys(code1)
        # sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/button').click()
        sleep(3)
    def member_list(self):

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/div/div/span').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/ul/li[1]/span').click()
        sleep(3)
        member_list1 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
        sleep(3)
        for i in range(len(member_list1)):
            member_name = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+']/td[2]/div').text
            sleep(3)
            member_mobile = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr['+str(i+1)+"]/td[3]/div").text
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[1]/div/input').send_keys(member_name)
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[1]/span').click()
            sleep(3)
            member_list2 = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
            sleep(3)

            for j in range(len(member_list2)):
                # member_name2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[' + str(j+1) + "]/td[2]/div").text
                member_mobile2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[' + str(j+1) + "]/td[3]/div").text
                if member_mobile == member_mobile2:
                    print(True)
                else:
                    print(False)
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[2]/span').click()
            sleep(3)




    def quit(self):
        self.driver.quit()





