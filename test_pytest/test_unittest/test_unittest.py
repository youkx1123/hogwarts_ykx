# 导入unittest
import unittest


# 测试类继承unittest.TestCase就可以，建议以test开头
# 驼峰命名方法
class TestSdemo(unittest.TestCase):
    # setUp和tearDown 方法是在每条测试用例前后分别调用
    def setUp(self) -> None:
        print(" setUP")

    def tearDown(self) -> None:
        print(" teardown")

    # setUpClass和tearDownClass是在整个类的前后分别调用的方法
    # setUpClass属于类级别的需要加上装饰器
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    # 用例以test开头
    def test_abc(self):
        print("test abc 11 ")

    def test_upper(self):
        print("upper 22")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("isupper 33")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("split 44")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
