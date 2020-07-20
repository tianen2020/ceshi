"""
1，完成一个商城购物车的程序。
商品信息在文件存储的，存储形式：
name price
电脑 1999
鼠标 10
游艇 20
美女 998
.......

要求:
1，用户先给自己的账户充钱：比如先充3000元。
2，读取商品信息文件将文件中的数据转化成下面的格式：
goods = [{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
...... ]

3，页面显示 序号 + 商品名称 + 商品价格，如：
1 电脑 1999
2 鼠标 10
…
n 购物车结算
q或者Q退出程序。

4，用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
5，如果用户输入的商品序号有误，则提示输入有误，并重新输入。
6，用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
7，用户输入Q或者q退出程序。
8，退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少，并将购买信息写入文件。

完成1-3要求为C。
完成1-4要求为 C+。
完成1-6要求为B。
完成全部要求并且没有BUG为A 或者A +。
"""

# 1，用户先给自己的账户充钱：比如先充3000元。
# with open("./shopping.txt",encoding="utf-8") as f:
#     for line in f:
#         print(line)
# with open("./shopping.txt",mode = "a+",encoding="utf-8") as f:
#     for line in f.readlines():
#         print(line)
# with open("./shopping.txt",mode = "a+",encoding="utf-8") as f:
#     f.write("大哥")

with open("./shopping.txt",mode = "r",encoding="utf-8") as f:
    li = []
    li1 = f.readline().split()
    for line in f:
        dic = {}
        new_line = line.strip('').split()
        print(new_line)
        for i in range(len(li1)):
            dic[li1[i]] = new_line[i]
        li.append(dic)
    print(li)






