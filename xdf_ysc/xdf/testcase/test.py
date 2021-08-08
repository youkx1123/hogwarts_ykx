
# from xdf_ysc.page.main import Main
from xdf_ysc.xdf.page import Base_page
from xdf_ysc.xdf.page.login_page import Login

class Testlogin:

    # def setup(self):
    #     self.main = Main()
    #
    # def test_login(self):
    #     assert self.main.goto_login().login()


    if __name__ == '__main__':
        Base_page().set_up()
        Login.longin()



