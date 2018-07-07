import mysql.connector

conn = mysql.connector.connect(user='root', password='amuluo', database='fantastic')
cursor = conn.cursor()

# user表创建
# cursor.execute('create table User (user_id int primary key,'
#                'user_name varchar(20),'
#                'user_password int,'
#                'user_loc_longitude float,'
#                'user_loc_latitude float,'
#                'user_time varchar(20),'
#                'user_remark char(80))')


# #测试用的
# cursor.execute('create table test (id int, '
#                'latitude float, '
#                'time varchar(20))')
# cursor.execute('insert into test (id, latitude, time) values (%s, %s, %s)', ['1', '5.5', '2016-12-15 16:48:40'])
# cursor.execute('drop table User')

# # user表添加
# cursor.execute('insert into User '
#                '(user_id, user_name, user_password, user_loc_longitude, user_loc_latitude, user_time, user_remark) '
#                'values (%s, %s, %s, %s, %s, %s, %s)',
#                ['1', 'chris', '123456', '115.25308', '39.261832', '2016-12-15 16:48:40', 'NULL'])
# cursor.execute('insert into User '
#                '(user_id, user_name, user_password, user_loc_longitude, user_loc_latitude, user_time, user_remark) '
#                'values (%s, %s, %s, %s, %s, %s, %s)',
#                ['2', 'paul', '23456', '117.23182', '40.12351', '2018-6-1 12:32:20', 'NULL'])
# cursor.execute('insert into User '
#                '(user_id, user_name, user_password, user_loc_longitude, user_loc_latitude, user_time, user_remark) '
#                'values (%s, %s, %s, %s, %s, %s, %s)',
#                ['3', 'james', '116.156123', '39.8321532', '1561.153', '2018-6-1 12:32:20', 'NULL'])
# cursor.execute('insert into User '
#                '(user_id, user_name, user_password, user_loc_longitude, user_loc_latitude, user_time, user_remark) '
#                'values (%s, %s, %s, %s, %s, %s, %s)',
#                ['4', 'harden', '23456', '117.153841', '41.025483', '2018-6-1 12:32:20', 'NULL'])
# cursor.execute('insert into User '
#                '(user_id, user_name, user_password, user_loc_longitude, user_loc_latitude, user_time, user_remark) '
#                'values (%s, %s, %s, %s, %s, %s, %s)',
#                ['5', 'bryant', '23456', '116.21681321', '39.512542', '2018-6-1 12:32:20', 'NULL'])


# # Shop表创建
# cursor.execute('create table Shop (shop_id int,'
#                'shop_name varchar(20),'
#                'shop_loc_longitude float,'
#                'shop_loc_latitude float,'
#                'shop_evaluate float,'
#                'shop_introduction varchar(100),'
#                'shop_remark varchar(100),'
#                'shop_category varchar(20))')

# # Shop表添加
# cursor.execute('insert into Shop '
#                '(shop_id, shop_name, shop_loc_longitude, shop_loc_latitude,'
#                'shop_evaluate, shop_introduction, shop_remark, shop_category) '
#                'values (%s, %s, %s, %s, %s, %s, %s, %s)',
#                ['1', '麦当劳', '115.62132', '39.884321', '4.5', '中国最受欢迎的西式快餐', 'NULL', '美食'])
# cursor.execute('insert into Shop '
#                '(shop_id, shop_name, shop_loc_longitude, shop_loc_latitude,'
#                'shop_evaluate, shop_introduction, shop_remark, shop_category) '
#                'values (%s, %s, %s, %s, %s, %s, %s, %s)',
#                ['2', '麦颂', '116.216123', '40.186123', '4.5', '一个很自由的唱歌场所', 'NULL', 'KTV'])
# cursor.execute('insert into Shop '
#                '(shop_id, shop_name, shop_loc_longitude, shop_loc_latitude,'
#                'shop_evaluate, shop_introduction, shop_remark, shop_category) '
#                'values (%s, %s, %s, %s, %s, %s, %s, %s)',
#                ['3', '大地影院', '116.81321', '41.018612', '4.5', '很好的电影院', 'NULL', '电影'])
# cursor.execute('insert into Shop '
#                '(shop_id, shop_name, shop_loc_longitude, shop_loc_latitude,'
#                'shop_evaluate, shop_introduction, shop_remark, shop_category) '
#                'values (%s, %s, %s, %s, %s, %s, %s, %s)',
#                ['4', '一健身', '116.4532', '41.82123', '4.5', '很好的健身房', 'NULL', '运动健身'])
# cursor.execute('insert into Shop '
#                '(shop_id, shop_name, shop_loc_longitude, shop_loc_latitude,'
#                'shop_evaluate, shop_introduction, shop_remark, shop_category) '
#                'values (%s, %s, %s, %s, %s, %s, %s, %s)',
#                ['5', '如家快捷酒店', '117.21861', '40.123845', '4.5', '很好吃的酒店', 'NULL', '酒店'])
# cursor.execute('insert into Shop '
#                '(shop_id, shop_name, shop_loc_longitude, shop_loc_latitude,'
#                'shop_evaluate, shop_introduction, shop_remark, shop_category) '
#                'values (%s, %s, %s, %s, %s, %s, %s, %s)',
#                ['6', '海底捞', '115.321382', '40.186123', '4.5', '中国最受欢迎的中式火锅', 'NULL', '美食'])

# # Friend表创建
# cursor.execute('create table Friend (user_id_1 int,'
#                'user_id_2 int)')
# # Friend表添加
# cursor.execute('insert into Friend (user_id_1, user_id_2)values (%s, %s)', ['1', '2'])
# cursor.execute('insert into Friend (user_id_1, user_id_2)values (%s, %s)', ['2', '1'])
# cursor.execute('insert into Friend (user_id_1, user_id_2)values (%s, %s)', ['1', '3'])
# cursor.execute('insert into Friend (user_id_1, user_id_2)values (%s, %s)', ['3', '1'])
# cursor.execute('insert into Friend (user_id_1, user_id_2)values (%s, %s)', ['4', '5'])
# cursor.execute('insert into Friend (user_id_1, user_id_2)values (%s, %s)', ['5', '4'])

# # Feature表创建
# cursor.execute('create table Feature (shop_id int,'
#                'feature_property varchar(20))')
#
# # Feature表添加
# cursor.execute('insert into Feature (shop_id, feature_property)values (%s, %s)', ['1', '小吃快餐'])
# cursor.execute('insert into Feature (shop_id, feature_property)values (%s, %s)', ['6', '火锅'])

# # Order表创建
# cursor.execute('create table OD (order_id int primary key,'
#                'user_id int,'
#                'shop_id int,'
#                'order_evaluate varchar(80))')
#
# # Order表添加
# cursor.execute('insert into OD (order_id, user_id, shop_id, order_evaluate)'
#                'values (%s, %s, %s, %s)', ['100', '1', '1', '不错'])


cursor.rowcount

conn.commit()
cursor.close()

cursor = conn.cursor()
# # user表测试
# cursor.execute('select * from User')
# # Shop表测试
# cursor.execute('select * from Shop')
# # Friend表测试
# cursor.execute('select * from Friend')
# # Feature表测试
# cursor.execute('select * from Feature')
# # Order表测试
cursor.execute('select * from OD')

values = cursor.fetchall()
print(values)



cursor.close()
conn.close()
