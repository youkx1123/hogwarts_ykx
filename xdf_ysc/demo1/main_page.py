from time import sleep

from xdf_ysc.demo1.test_page import TestWebPage
from xdf_ysc.demo1.test_page506 import TestWebPage1

if __name__ == '__main__':

    # TestPage = TestWebPage()
    # TestPage.login('https://test-staff.xdfgk.cn/login', '18510929499', 'xdf_929499')
    # TestPage.member_list()


    TestPage2 = TestWebPage1()
    TestPage2.login('https://test-staff.xdfgk.cn/login', '18510929499', 'xdf_929499')
    TestPage2.member_list()



    sleep(3)
    TestPage2.quit()


