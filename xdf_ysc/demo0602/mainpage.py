import time

from xdf_ysc.demo0602.testpage import TestPage

if __name__ == '__main__':
    TestPage1 = TestPage()
    TestPage1.longin_page("https://test-staff.xdfgk.cn/accounts/staff/", '18510929499', 'xdf_929499')

    TestPage1.member_list_page()

    time.sleep(4)
    TestPage1.quit()