from test_web05.page_object12.main import Main


class Test1:
    def test(self):
        main = Main()
        main.click_first_link().title()
