# -*- codeing = utf-8 -*-
# @Time     :2021/4/21
# @Author   :ly
# @File     :listeg.py
# @Spftware :PyCharm
import random

# 把names 随机分到offce 并遍历出来
# offces =[[],[],[]]
# names=["A","B","C","D","E","F","g"]
'''
for name in names:
    num = random.randint(0,2)
    offces[num].append(name)
a = 0
for offce in offces:
    print("a%d号办公室里有%d名老师，分别为"%(a,len(offce)))
    a += 1
    for name in offce :
        print("%s"%name,end="\t")
        print("\n")
        print("~"*20)
'''


products =[["iphone",6888],["MACPRO",14888],["小米",24000],['Coffee',31],["book",60]]

mailist =[]

x = True
while x :
 print("-"*5+"商品列表"+"-"*5)
 for p in products:
        print( str(products.index(p) + 1) + "\t" + str(p[0]) + "\t" +  str(p[1]))
 inpurIndex = int(input("你想买什么?"))

 # while not inpurIndex.isdigit():
 #        inpurIndex = input("请输入数字编码：")
 mailist.append(products[inpurIndex - 1])
 if len(mailist) >3:
     x = False

print("-"*5+"购买列表"+"-"*5)
for p in mailist:
    print( str(products.index(p) + 1) + "\t" + str(p[0]) + "\t" +  str(p[1]))
