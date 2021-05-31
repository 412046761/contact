# -*- codeing = utf-8 -*-
# @Time     :2021/4/26
# @Author   :ly
# @File     :urllibTest.py
# @Spftware :PyCharm
import urllib.request

# get请求
# responce = urllib.request.urlopen("https://www.baidu.com/");
# print(responce.read().decode('utf-8'))

# post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"word"}),encoding="utf-8")
# responce = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(responce.read().decode('utf-8'))

# 超时处理
# try:
#     responce = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(responce.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print('time out')

# 消息头
# responce = urllib.request.urlopen("http://www.baidu.com")
# print(responce.status) # 状态码 200 正常 418 发现爬虫
# print(responce.getheaders())
# 获取header某个属性
# print(responce.getheader('Bdpagetype'))

# 组装信息
# url = 'http://httpbin.org/post'
# data = bytes(urllib.parse.urlencode({"hello":"word"}),encoding="utf-8")
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# url = 'https://www.douban.com'
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
# req = urllib.request.Request(url=url,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

url = 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg'
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))