from time import sleep


class Login_Page:
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