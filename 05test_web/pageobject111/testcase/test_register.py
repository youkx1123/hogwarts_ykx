from pageobject.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        # 列式调用
        assert self.main.goto_register().register()
