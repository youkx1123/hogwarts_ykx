import unittest

if __name__ == '__main__':
    # 方法四 匹配某个目录下所有的以test开头的py文件，执行这个文件下的所有测试用例
    # discover可以一次调用多个版本，test_dir被测试脚本的路径，pattern脚本名称匹配规则
    test_dir = ''
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)
