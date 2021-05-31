# -*- codeing = utf-8 -*-
# @Time     :2021/5/21
# @Author   :ly
# @File     :testSqlite.py
# @Spftware :PyCharm
import sqlite3


# 2.创建数据表
conn = sqlite3.connect("test.db")   # 数据库连接
print('成功打开数据库')
c = conn.cursor()                   # 获取游标
sql = '''
    create table company
      (id int primary key not null,
       name text not null ,
       age int not null,
       address char(50),
       salary real);
'''

c.execute(sql)                      # 执行SQL
conn.commit()                       # 提交数据库操作
conn.close()                        # 关闭数据库连接
print('成功建表')

