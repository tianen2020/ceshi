# 当给函数传入的参数数目不定时，使用动态参数，万能参数
# def eat(args,a,b="asd",c="dasd"):
#     print(f"{args}-{b}-{c}")
#     return
# print(eat("猪蹄","红烧肉","a"))
"""
1.位置参数
2.关键字参数
3.混合参数

1.位置参数
2.默认参数
3.*args 动态参数 返回的是一个元组 *把所有的实参的位置参数在形参是聚合生成一个元组
"""
# def eat(*args,**kwargs):
#     print(f"{args}")
#     print(f"{kwargs}")
#     return
# print(eat("猪蹄","红烧肉","a",b=1,c=2))

# def sum(*args):
#     sumi = 0
#     for i in args:
#         sumi = sumi +i
#     return sumi
# print(sum(1,4,6,67,55,11))


# dic= {"K":"asd","hh":"12we","kke":"qwe"}
# for i in dic:
#     print(i)
#     del dic["K"]
# print(dic)

li = [1,2,546,76]
for i in  li:
    del li[1]
print(li)