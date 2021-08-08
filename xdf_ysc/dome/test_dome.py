from time import sleep
from selenium import webdriver


class PyWeb:


    def __init__(self):
        self.driver = webdriver.Chrome()
    # 登录页面
    def login(self, url):
        print(url)
        self.driver.get(url)
        # self.driver.get("https://test-staff.xdfgk.cn/login")
        self.driver.implicitly_wait(3)
        # self.driver.maximize_window()
        # 用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div/input').send_keys("18510929499")
        # 密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input').send_keys("xdf_929499")
        # 登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/button').click()
        sleep(3)
    # 员工列表页面
    def member_list(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/div/div').click()
        sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div[1]/li/ul/li[1]/span').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[1]/div/input').send_keys('刘')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[1]/span').click()
        sleep(3)
        # 序号
        a = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div').text
        # 手机号
        b = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div').text
        # 查询个数
        count=len(self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr'))
        print(count)
        #
        r = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr')
        print("r是：", r)
        # for i in range(len(r)):
        #     print(r[i][3])

        # self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]')



        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[2]/span').click()
        sleep(3)

    def add_members(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button[4]/span').click()
        sleep(3)

    def quit(self):
        self.driver.quit()

    # def __del__(self):
        # self.driver.quit()


    # def pp(self):
    #     print(1)
