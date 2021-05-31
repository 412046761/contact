# -*- codeing = utf-8 -*-
# @Time     :2021/4/22
# @Author   :ly
# @File     :file.py
# @Spftware :PyCharm

# f = open("test.txt","w")    # 打开文件 w 写模式
# f.write("hello world,i am here!")
# f.close() # 关闭

# f = open("test.txt","r")
# print(f.read(5))
# print(f.readlines())
# f.close() # 关闭

# f = open("test.txt","r")
# i = 1
# for temp in f.readlines():
#     print("%d:%s"%(i,temp))
#     i += 1
# f.close() # 关闭


# f = open("test.txt","r")
# print(f.readline())
# print(f.readline())
# f.close() # 关闭

import os
# os.rename("test.txt","test1.txt") #改名
# os.remove("test.txt") #删除文件
# os.rmdir("") #删除文件夹
# os.listdir("xx./") #获取目录列表
# os.getcwd()#获取当前目录
# os.chdir("../") #改变目录
# os.mkdir('douban/jpg/123')#创建文件夹
# print(os.path.exists('douban/jpg/123')) #是否存在文件夹

