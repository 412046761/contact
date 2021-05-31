# -*- codeing = utf-8 -*-
# @Time     :2021/4/28
# @Author   :ly
# @File     :bs4Test.py
# @Spftware :PyCharm

'''
BeavtifulSoup4 将复杂HTML文档转化成一个复杂的树形结构，每个节点都是Python对象，对所有对象可以归纳为4种：

- Tag
- NavigableString
- BeautifulSoup
- Comment
'''
import re

from bs4 import BeautifulSoup

file = open("./temp.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

# 1.Tag 标签及其内容：拿到它找到的第一个内容
# print(bs.title)
# print(bs.a)


# 2.NavigableString 单纯内容，无标签(字符串)
# print(bs.title.String)
# print(type(bs.title.String))
# print(bs.a.attrs)

# 3.BeautifulSoup 表示整个文档
# print(type(bs))
# print(bs)

# 4.Comment 是一个特殊的NavigableString，输出的内容不包含注释
# print(bs.a.string)
# print(type(bs.a.string))


#-----------------------------

# 文档的遍历
# head 内容
# print(bs.head.contents)
# head 的一个元素
# print(bs.head.contents[1])
# 更多内容搜索文档

# 文档的搜索

# 1.find_all()   字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list)

# 正则表达式搜索：使用Search() 方法来匹配内容 包含a的
# t_list= bs.find_all(re.compile("a"))
# print(t_list)

# 方法 ： 传入一个函数,根据函数的要求来搜索 (了解)
# def name_si_exists(tag):
#     return  tag.has_attr("name")
#
# t_list =bs.find_all(name_si_exists)
#
# print(t_list)

# 2.kwargs 参数
# t_list = bs.find_all(id="head")

# for item in t_list:
#     print(t_list)

# 3.text参数

# t_list = bs.find_all(text="好123")
# t_list = bs.find_all(text=["好23","地图","贴吧"])
# t_list = bs.find_all(text=re.compile("\d")) #应用正则表达式查找特定的文本内容

# 4.limit 参数
# t_list = bs.find_all("a",limit=3)
#
# for item in t_list:
#     print(t_list)

# css选择器
t_list = bs.select('title') # 标签查找
t_list = bs.select('.mnav') # 类名查找
t_list = bs.select('#u1') # id查找
t_list = bs.select("a[class='bri']") # 属性查找
t_list = bs.select("head > title") # 通过层级来查找
t_list = bs.select(".mnav ~ .bri") # 通过子标签来查找

for item in t_list:
    print(t_list)