import unittest


class Search:

    def search_fun(self):
        print("search  11")
        return True


class TestSearch(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) ->None:
    #     print("setUpClass")
    #     cls.search=Search()
    #
    # @classmethod
    # def tearDownClass(cls) ->None:
    #     print("tearDownClass")

    def setUp(self):
        print("setUp ******")
        self.search = Search()

    def tearDown(self):
        print("setdown  ****** ")

    def test_search1(self):
        print("tset_search1")
        # 实例化一个类
        # search=Search()
        # 断言
        assert True == self.search.search_fun()

    def test_search2(self):
        print("tset_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("tset_search3")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 1, "verify 判断 1 == 1")

    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1, 2, "verify 判断 1 != 2")


class TestSearch1(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) ->None:
    #     print("setUpClass")
    #     cls.search=Search()
    #
    # @classmethod
    # def tearDownClass(cls) ->None:
    #     print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.search = Search()

    def tearDown(self):
        print("setdown")

    def test_search1(self):
        print("tset_search1")
        # 实例化一个类
        # search=Search()
        # 断言
        assert True == self.search.search_fun()

    def test_search2(self):
        print("tset_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("tset_search3")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 1, "verify 判断 1 == 1")

    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1, 2, "verify 判断 1 != 2")


class TestSearch2(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) ->None:
    #     print("setUpClass")
    #     cls.search=Search()
    #
    # @classmethod
    # def tearDownClass(cls) ->None:
    #     print("tearDownClass")

    def setUp(self):
        print("setUp--------")
        self.search = Search()

    def tearDown(self):
        print("setdown-------")

    def test_search1(self):
        print("tset_search1")
        # 实例化一个类
        # search=Search()
        # 断言
        assert True == self.search.search_fun()

    def test_search2(self):
        print("tset_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("tset_search3")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 1, "verify 判断 1 == 1")

    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1, 2, "verify 判断 1 != 1")


if __name__ == "__main__":
    # 方法一，执行当前文件所有的unittest测试用例，全部执行
    # unittest.main()
    #
    # #方法二，执行指定的测试用例，将要执行的测试用例添加到套件里面，批量执行测试方法
    # #创建一个测试套件，testsuite
    # suite=unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # unittest.TextTestRunner().run(suite)

    # 方法三，执行某个测试类,将测试类添加到测试套件里面，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
