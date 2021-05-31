# -*- codeing = utf-8 -*-
# @Time     :2021/4/22
# @Author   :ly
# @File     :fangfa.py
# @Spftware :PyCharm

'''
# 无参方法
def tip():
    print("-" * 10)
    print("我用python")
    print("-" * 10)
tip()
'''
# 有参方法
def sum(a,b):
    return a+b
print(sum(1,2))

#多返回值方法
def chu(a,b):
    shang = a // b
    yu =  a % b
    return shang,yu

sh,yu=chu(5,2)
print("商：%d,余：%d"%(sh,yu))