from xdf_ysc.test0603.testpage import TestPage

if __name__ == '__main__':
    TestPage1 = TestPage()
    TestPage1.login("https://test-staff.xdfgk.cn/accounts/staff/", "18510929499", "xdf_929499")
    TestPage1.member_list()


    TestPage1.quit()