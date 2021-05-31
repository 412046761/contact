# -*- codeing = utf-8 -*-
# @Time     :2021/5/21
# @Author   :ly
# @File     :testSqliteSQLinsert.py
# @Spftware :PyCharm
import sqlite3

# insert 语句
# conn = sqlite3.connect('test.db');
# print('连接成功数据库')
# n = conn.cursor()
# sql = '''
#  insert into company (id,name,age,address) values(1,'test',11,'shanxi');
# '''
# n.execute(sql)
# conn.commit()
# conn.close()
# print('数据插入成功')


# SELECT
conn = sqlite3.connect('test.db');
print('连接成功数据库')
n = conn.cursor()
sql = '''
SELECT * FROM COMPANY
'''
rs = n.execute(sql)
for row in rs:
    print("id ",row[0])
    print("name ", row[1])
    print("age ", row[2])
    print("address ", row[3])
conn.close()

