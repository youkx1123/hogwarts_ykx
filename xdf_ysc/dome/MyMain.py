from test_dome import PyWeb

if __name__ == '__main__':
    py1 = PyWeb()
    py1.login("https://test-staff.xdfgk.cn/login")
    username = py1.member_list()

    py1.add_members()


    py1.quit()