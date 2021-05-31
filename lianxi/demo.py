# -*- codeing = utf-8 -*-
# @Time     :2021/4/20
# @Author   :ly
# @File     :demo.py
# @Spftware :PyCharm

'''
# 输出
print("hello ly")
a = "hello ly"
print("%s 注入字符串" % a)
print("空格", end="\t")
print("回车", end="\n")
print("hello3")
'''

'''
# 输入
password = input("输入密码: ")
print("输入的密码是; ", password)
print(type(password))
# 字符串转为数字
c = int(password)
print(type(c))
'''

'''
# 判断
a=3
if(a<3):
    print("a<3 and 0<a")
elif(a<2):
    print("a<2 and 0<a")
else:
    print("false")
'''

'''
#循环

# 循环 i=0 i++ 5次循环
# for i in range (5):
#     print(i)

# i=0 i+3 i<10
# for i in range(0,10,3):
#     print(i)

# name = "chenge"
# for x in name:
#     print(x,end="\t")

# a = ["aa","bb","cc","dd"]
# for i in range(len(a)):
#     print(i,a[i])

# i = 0
# while i < 5:
#     print(i)
#     i += 1

'''

'''
# 字符串
a = 'a\'sd'
b = "阿斯皇帝"
c = """
    这是一个段落
            可ui随便格式哦
               哈哈
"""
print(a)
print(b)
print(c)

'''

'''
c ='change'
print(c)
print(c[0])
print(c[0:5])
# 起，终，步进
print(c[0:5:2])
print(c[5:])
print(c[:5])
'''

'''
c ='change'
print(c *3)
print(c +"你好")
print('hello\nchenge')
print(r'hello\nchenge')
'''
'''
# list
# namelist = ['张三','李四','王五']
# testlist = [1,'测试']
# 增
# namelist.append("赵六")      # 增加元素
# namelist.extend(testlist)   # 倒入
# namelist.insert(0,3)        # 指定下标插入元素
# 删
# del namelist[0]           # 指定下标删除
# namelist.remove('李四')    # 直接删除指定内容的元素 重复也只删除一个
# namelist.pop              #  弹出最后一个元素
# 改
# namelist[3] = 'asd'
# 查
# findname = input("请输入要查的名字")
# if findname in namelist:            # list中是否包含元素
#     print("名单里有")
# print(namelist.index('张三',0,4))  # 范围区间 【0 ， 4）中 ’张三‘的坐标
# print(namelist.count('张三'))      # list 中某元素的个数
# 排序
# namelist.sort()         #从小到大
# namelist.reverse()      #顺序反转
# namelist.sort(reverse=True) #从大到小



# print(type(testlist[0]))
# print(type(testlist[1]))
# print(namelist[0])

# for name in namelist:
#     print(name)
'''

# tuple 元组 子元素不允许修改
# tup1 = () # 空元组
# tup2 = (50) #不是元组
# tup2 = (50,) #元组

# 增
# tup1 = (12,34,56)
# tup2 = ("abc","xyz")
# tup = tup1 + tup2
# print(tup)
# 删
# tup1 = (12,34,56)
# print(tup1)
# del tup1
# print(tup1)
# 改
# tup1[0] =100 #报错 不允许修改
# 查 同list

# dict 字典
info = {"name":"吴彦祖","age":18}
# print(info["name"])
#
# # 字典Key不存在ag 返回mmm
# print(info.get("ag","mmm"))
info["sex"] = 'nan'
print(info["sex"])

# 增
# info["sex"] = 'nan'
# print(info)
# 删
# del info["sex"]
# print(info)
# 改
# info["sex"] = '男'
# print(info)
# 查
# print(info.keys()) # K
# print(info.values()) # V
# print(info.items()) # 子项

# 遍历
# for key,value in info.items():
#     print("key=%s,value=%s"%(key,value))

# Set 集合 无序 不可重复 只有K 无V
