import unittest
from case import *
# 加载测试用例到测试suit中，创建一个测试集对象
suit =unittest.TestSuite()
# suit.addTest(TestAdd("test_001"))
# suit.addTest(TestAdd("test_002"))
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(TestAdd))
# 运行测试用例
with open("a.txt","w") as file:
    runner = unittest.TextTestRunner(stream=file,verbosity=2)
    runner.run(suit)