# -*- coding:utf-8 -*-

import mysql
import pymysql
import mysql.connector
import sqlalchemy
from PIL import Image
import json
import requests

# 导入:
from sqlalchemy import Column, String, create_engine, Float, DateTime, func, Integer
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
    pic_id = Column(Integer)
    loc_longitude = Column(Float)
    loc_latitude = Column(Float)
    time = Column(DateTime, default=datetime.datetime.now)


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    address = Column(String(40))
    loc_longitude = Column(Float)
    loc_latitude = Column(Float)
    evaluate = Column(Float)
    introduction = Column(String(100))
    category = Column(String(20))
    path = Column(String(40))


class Friend(Base):
    __tablename__ = 'friend'

    id_1 = Column(String(20), primary_key=True)
    id_2 = Column(String(20))


class Feature(Base):
    __tablename__ = 'Feature'

    shop_id = Column(String(20), primary_key=True)
    property = Column(String(20))


class Order(Base):
    __tablename__ = 'Order'

    id = Column(String(20), primary_key=True)
    # user_id = Column(String(20))
    shop_id = Column(String(20))
    evaluate = Column(Float)
    time = Column(DateTime, default=datetime.datetime.now)
    suggest = Column(String(100))


class Participant(Base):
    __tablename__ = 'Participant'

    order_id = Column(String(20), primary_key=True)
    user_id = Column(String(20), primary_key=True)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:amuluo@localhost:3306/test3')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def add_user(name, password, pic_id, loc_longitude, loc_latitude):
    session = DBSession()
    new_id = session.query(func.count(User.id)).scalar() + 1
    new_user = User(id=new_id, name=name, password=password, pic_id=pic_id,
                    loc_longitude=loc_longitude, loc_latitude=loc_latitude)
    session.add(new_user)
    session.commit()
    session.close()


def add_shop(name, address, loc_longitude, loc_latitude, evaluate, introduction, category, path_):
    session = DBSession()
    new_id = session.query(func.count(Shop.id)).scalar() + 1
    new_shop = Shop(id=new_id, name=name, address=address, loc_longitude=loc_longitude, loc_latitude=loc_latitude,
                    evaluate=evaluate, introduction=introduction, category=category, path=path_)
    session.add(new_shop)
    session.commit()
    session.close()


def add_friend(id_1, id_2):
    session = DBSession()
    new_friend = Friend(id_1=id_1, id_2=id_2)
    session.add(new_friend)
    session.commit()
    session.close()


def add_feature(f_id, kind):
    session = DBSession()
    new_feature = Feature(shop_id=f_id, kind=kind)
    session.add(new_feature)
    session.commit()
    session.close()


def add_order(o_id, shop_id, evaluate, suggest):
    session = DBSession()
    new_order = Order(id=o_id, shop_id=shop_id, evaluate=evaluate, suggest=suggest)
    session.add(new_order)
    session.commit()
    session.close()


def add_participant(order_id, user_id):
    session = DBSession()
    new_participant = Participant(order_id=order_id, user_id=user_id)
    session.add(new_participant)
    session.commit()
    session.close()


# # 建表操作
Base.metadata.create_all(engine)


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


def search_login_get_password(username):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.name == username).one()
    # 关闭Session:
    session.close()
    return user.password


def search_login_get_loc(username):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.name == username).one()

    # 关闭Session:
    session.close()
    return user.loc_longitude, user.loc_latitude


if __name__ == '__main__':
    num = 1
    # while(1):
    #     name_ = input("enter shop name:")
    #     address_ = input("enter shop address:")
    #     result = get_loc(address_)
    #     evaluate_ = input("enter shop evaluate:")
    #     introduction_ = input("enter shop introduction:")
    #     category_ = input("enter shop category:")
    #     path = "/picture/"+str(num)+".jpg"
    #     add_shop(name_, address_, result['lng'], result['lat'], evaluate_, introduction_, category_, path)
    #     num = num + 1
    # s = Image.open("C:/Users/1996j/Desktop/1.jpg")
    # s.show()
    print(search_login_get_password('111'))