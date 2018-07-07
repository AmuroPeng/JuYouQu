# -*- coding:utf-8 -*-

import mysql
import pymysql
import mysql.connector
import sqlalchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 连接数据库
conn = mysql.connector.connect(user='root', password='amuluo', database='test')
cursor = conn.cursor()
# 建表
cursor.execute('create table Users (user_id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into Users (id, name) values (%s, %s)', ['1', 'Michael'])
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
print(1111111111)
# conn = mysql.connector(user='root',password='amuluo',database='test')
# cursor = conn.cursor()
# # 执行查询语句:
# cursor.execute('select * from user where id=?', ('1',))
# # 获得查询结果集:
# values = cursor.fetchall()
# values
# cursor.close()
# conn.close()
