# -*- codeing = utf-8 -*-
# @Time     :2021/4/23
# @Author   :ly
# @File     :errEx.py
# @Spftware :PyCharm

try:
 r = open("123.txt","r")

except Exception as result:
    print("打开错误了")
    print(result)