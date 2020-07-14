from configparser  import ConfigParser
# # 创建一个配置文件的对象
# cf = ConfigParser()
# # 读取配置文件
# cf.read("./demo.cfg",encoding="utf-8")
# # 读取所有的section
# se = cf.sections()
# # print(se)
# # 根据section 获取所有的options
# ops = cf.options(se[1])
#
# print(ops)
# # 根据setion 和 option 得到value
# value = cf.get(se[1],ops[5])
# print(value)
class myConfig:
    def __init__(self,conf_path,encoding="utf-8"):
        # 实例化一个config对象打开一个配置文件
        self.cf = ConfigParser()
        self.cf.read(conf_path)

    def get_section(self):
        # 读取所有的section
        se = self.cf.sections()
        return se
    def get_options(self,section):
        # 读取所有的section下的option
        se1 = self.cf.options(section)
        return se1
    def get(self,section,option):
        value = self.cf.get(section,option)
        return value
"""
TestCase   这个类专门写测试用例的,使用继承去写测试用例
TestSuite  从TestCase收集测试用例
TestLoader 加载测试用例或者测试用例集
TestRunner 运行测试用例
TestResult 生成测试报告 
这个类的实例（对象）是一个单独的测试用例
"""
