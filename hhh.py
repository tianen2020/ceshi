import  requests
import json
# s = requests.Session()
# params = {
#     "clientId":"2019022814080064",
#     "responseType":"code",
#     "selfSign":"true",
#     "sysTag":"HIS",
# }
# res = s.get("https://beta.51trust.com/gateway/oauth/authorize",params = params)
# # print(res.text) # 返回是一个response对象的实体 里面包括 请求头 行 体啊 状态码
# res_json = res.json()
# # print(res_json)
# # print(res.cookies)
# imgbase64 = res_json['data']['imgBase64']
# print(imgbase64)
# session = requests.sessions.Session()
# s = session.request()
# """
# openid 转换成uniqueid
# """
# openid = "ddd9c56374debf68qbb44w0307y3dcb806b"
#
#
# uniqueid = "b608bcd3703044bb86fbed47365c9ddd"
# def openid_uniqueid(openid):
#     # 切片掉字符串的
#
# openid_uniqueid("ddd9c56374debf68qbb44w0307y3dcb806b")