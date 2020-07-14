import unittest
from excel import get_data
from ddt import ddt,data,unpack
from data_test import data_test
# 这个类的实例（对象）是一个测试用例
"""
  单元测试，导入要测试的类进行调用
"""
@ddt
class TestAdd(unittest.TestCase):

    @data(*get_data())
    @unpack
    def test_001(self,a,b,expect):
        print("a",a)
        print("b",b)
        expect = expect # 期望结果
        print(expect)
        # 断言预期结果的比对



