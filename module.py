# -*- coding:utf-8 -*-

import SpatialRelaiton
from pos_generation import get_loc
from pos_generation import get_navi

# 导入:
from sqlalchemy import Column, String, create_engine, Float, DateTime, func, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
import time

length = 100

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(length), primary_key=True)
    name = Column(String(length))
    password = Column(String(length))
    pic = Column(String(length))
    loc_lng = Column(Float)
    loc_lat = Column(Float)
    time = Column(DateTime, default=datetime.datetime.now)


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(String(length), primary_key=True)
    name = Column(String(length))
    address = Column(String(length))
    loc_lng = Column(Float)
    loc_lat = Column(Float)
    evaluate = Column(Float)
    introduction = Column(String(length))
    category = Column(String(length))
    pic = Column(String(length))


class Friend(Base):
    __tablename__ = 'friend'

    id_1 = Column(String(length), primary_key=True)
    id_2 = Column(String(length), primary_key=True)


class Feature(Base):
    __tablename__ = 'Feature'

    shop_id = Column(String(length), primary_key=True)
    property = Column(String(length))


class Order(Base):
    __tablename__ = 'Order'

    id = Column(String(length), primary_key=True)
    # user_id = Column(String(length))
    shop_id = Column(String(length))
    evaluate = Column(Float)
    time = Column(DateTime, default=datetime.datetime.now)
    suggest = Column(String(length))  # 存推荐内容


class Participant(Base):
    __tablename__ = 'Participant'

    order_id = Column(String(length), primary_key=True)
    user_id = Column(String(length), primary_key=True)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:amuluo@localhost:3306/test3')
# 使用服务器时用此连接：
# engine = create_engine('mysql+mysqlconnector://root:amuluo@127.0.0.1:3306/test3')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def add_user(name, password, pic, loc_lng, loc_lat):
    session = DBSession()
    new_id = session.query(func.count(User.id)).scalar() + 1
    new_user = User(id=new_id, name=name, password=password, pic=pic,
                    loc_lng=loc_lng, loc_lat=loc_lat)
    session.add(new_user)
    session.commit()
    session.close()
    return new_id


def add_shop(name, address, loc_lng, loc_lat, evaluate, introduction, category, pic):
    session = DBSession()
    new_id = session.query(func.count(Shop.id)).scalar() + 1
    new_shop = Shop(id=new_id, name=name, address=address, loc_lng=loc_lng, loc_lat=loc_lat,
                    evaluate=evaluate, introduction=introduction, category=category, pic=pic)
    session.add(new_shop)
    session.commit()
    session.close()


def add_friend(id_1, id_2):
    session = DBSession()
    new_friend_1 = Friend(id_1=id_1, id_2=id_2)
    new_friend_2 = Friend(id_1=id_2, id_2=id_1)
    session.add(new_friend_1)
    session.add(new_friend_2)
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


def add_participant_create_id(user_id):
    session = DBSession()
    print(session.query(func.count(Order.id)).scalar())
    new_id = session.query(func.count(Order.id)).scalar() + 1
    print(new_id)
    new_participant = Participant(order_id=new_id, user_id=user_id)
    session.add(new_participant)
    session.commit()
    session.close()
    return new_id


def add_participant(order_id, user_id):
    session = DBSession()
    new_participant = Participant(order_id=order_id, user_id=user_id)
    session.add(new_participant)
    session.commit()
    session.close()


# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob', password='123456', loc_lng=1.1, loc_lat=0.1)
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


def search_user_get_password(username):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.name == username).one()
    # 关闭Session:
    session.close()
    return user.password


def search_user_name_get_loc(username):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.name == username).one()
    user.time = datetime.datetime.now()
    x = user.loc_lng
    y = user.loc_lat
    session.commit()
    session.close()
    return x, y


def search_user_id_get_loc(user_id):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.id == user_id).one()
    user.time = datetime.datetime.now()
    x = user.loc_lng
    y = user.loc_lat
    session.commit()
    session.close()
    return x, y


def search_user_get_all(user_id):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.id == user_id).one()
    session.close()
    return user


def search_shop_get_loc(shop_id):
    session = DBSession()
    shop = session.query(Shop).filter(Shop.id == shop_id).one()
    x = shop.loc_lng
    y = shop.loc_lat
    session.close()
    return x, y


def search_user_get_id(username):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.name == username).one()
    result_id = user.id
    session.close()
    return result_id


def search_user_get_order_list(user_id):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    users = session.query(Participant).filter(Participant.user_id == user_id).all()
    result = []
    for user in users:
        results = session.query(Order).filter(Order.id == user.order_id).one()
        result.append({'id': results.id, 'content': results.suggestion})
    session.close()
    return result


def search_friend_get_list(search_id):
    session = DBSession()
    list = session.query(Friend).filter(Friend.id_1 == search_id).all()
    result = []
    for i in list:
        user = session.query(User).filter(User.id == i.id_2).one()
        count_time = int(((datetime.datetime.now() - user.time).total_seconds()) / 3600)
        result.append({'id': user.id, 'name': user.name, 'time': count_time, 'pic': user.pic,
                       'loc_lng': user.loc_lng, 'loc_lat': user.loc_lat})
    session.close()
    return result


def search_shop_get_id_list(friend_loc_list):
    session = DBSession()
    shop_list_all = session.query(Shop).all()
    session.close()
    result = {}
    i = 0
    for shop in shop_list_all:
        if SpatialRelaiton.isPolygonContainsPoint(friend_loc_list, [shop.loc_lng, shop.loc_lat]):
            count = 0
            for friend in friend_loc_list:
                way, temp_count = get_navi(friend[0], friend[1], shop.loc_lng, shop.loc_lat)
                count += temp_count
            if count < 1000000000:  # 如果报错查询不到的话，直接忽略
                result[shop.id] = count
    result_sorted = sorted(result.items(), key=lambda d: d[1])
    result_list = []
    for i in result_sorted:
        result_list.append(int((list(i))[0]))
    return result_list


def search_shop_get_info_dict(id_list):
    session = DBSession()
    result = {}
    for i in id_list:
        shop = session.query(Shop).filter(Shop.id == i).one()
        result[i] = {'id': shop.id, 'name': shop.name, 'address': shop.address, 'evaluate': shop.evaluate,
                     'category': shop.category,
                     'pic': shop.pic, 'introduction': shop.introduction}
    session.close()
    return result


def search_shop_get_info_list(id_list):
    session = DBSession()
    result = []
    for i in id_list:
        shop = session.query(Shop).filter(Shop.id == i).one()
        result.append({'id': shop.id, 'name': shop.name, 'address': shop.address, 'evaluate': shop.evaluate,
                       'category': shop.category, 'pic': shop.pic, 'introduction': shop.introduction})
    session.close()
    return result


# def search_():
#     # 创建Session:
#     session = DBSession()
#     # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
#     user = session.query(User).filter(User.name == username).one()
#     # 关闭Session:
#     session.close()
#     return user.loc_lng, user.loc_lat


if __name__ == '__main__':
    num = 1
    # 建表操作
    # Base.metadata.create_all(engine)

    # x1, y1 = search_user_get_loc('111')
    # x2, y2 = search_user_get_loc('222')
    # x3, y3 = search_user_get_loc('333')
    # x4, y4 = search_user_get_loc('444')
    # result = search_shop_get_id_list([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    # print(result)

    # print(search_shop_get_info_dict([12, 2, 3, 5]))

    # add_order(1, 2, 3, '特别好')
    # add_order(2, 3, 5, '特别不好')
    # add_order(3, 4, 1, '特别好')
    #
    # add_participant(1, 1)
    # add_participant(1, 2)
    # add_participant(1, 3)
    # add_participant(2, 1)
    # add_participant(2, 2)
    # add_participant(3, 2)
    # add_participant(3, 3)

    print(add_participant_create_id(2))