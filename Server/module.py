# -*- coding:utf-8 -*-

import mysql
import pymysql
import mysql.connector
import sqlalchemy

# 导入:
from sqlalchemy import Column, String, create_engine, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    password = Column(String(20))
    loc_longitude = Column(Float)
    loc_latitude = Column(Float)
    time = Column(DateTime, default=datetime.datetime.utcnow)


# 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://root:amuluo@localhost:3306/test2')
# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

# # 建表操作
# Base.metadata.create_all(engine)

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob', password='123456', loc_longitude=1.1, loc_latitude=0.1)
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()
#
# # 创建Session:
# session = DBSession()
# # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id == '5').one()
# # 打印类型和对象的name属性:
# print('type:', type(user))
# print('name:', user.name)
# # 关闭Session:
# session.close()
