# 用户登陆（三次输入机会)且每次输入错误显示剩余次数（提示：使用字符串格式化）
"""
分析：得有个循环，到了3次退出循环
     用户登陆输入 用户名和密码，只要有个错误就减少一次机会
"""
# count = 1
# while count <= 3:
#     username = input("请输入用户名\n")
#     password = input("请输入密码\n")
#     if username == "putianen" and password == "123456":
#         print("登陆成功")
#         break
#     else:
#         print("用户名或密码错误，你还有{}次机会".format(3-count))
#     count = count +1
# for i in range(1,4):
#     username = input("请输入用户名\n")
#     password = input("请输入密码\n")
#     if username == "putianen" and password == "123456":
#         print("登陆成功")
#         break
    # else:
    #     print("用户名或密码错误，你还有{}次机会")


# for i  in range(1,4,1):
#     username = input("请输入用户名\n")
#     password = input("请输入密码\n")
#     print(i) # 1 2 3
#     # 使用标记位记录输入次数
#     n = 3-i
#     if username == "putianen" and password == "123456":
#         print("登陆成功")
#         break
#     else:
#         print("用户名或密码错误，你还有{}次机会".format(n))


