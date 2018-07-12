# coding=utf8
# -*- coding:utf-8 -*-

from flask import Flask, render_template, flash, redirect, jsonify, url_for
from flask import request, session
import form
import module
import json
import logging
import pos_generation
import SpatialRelaiton
from sqlalchemy.orm import class_mapper

app = Flask(__name__)
app.secret_key = '111'


# 全局变量
# friend_dict = {}  # 好友列表（包含位置）


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = form.LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if password == module.search_user_get_password(username):
            print('密码正确')
            session['lng'], session['lat'] = module.search_user_name_get_loc(username)  # 并且更新了时间
            session['id'] = module.search_user_get_id(username)
            session['username'] = username
            print(session['lng'])
            return redirect('/')
        else:
            flash('用户名或密码错误')
    return render_template('login.html', login_form=login_form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = form.SignupForm()
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        loc = request.form.get('loc')

        pos = pos_generation.get_loc(loc)

        if not all([username, password, password2]):
            flash("参数不完整")
        elif password != password2:
            flash('密码不一致')
        elif type(pos) == str:
            flash(pos)
        else:
            temp_pic_path = '/source/picture/icon/1.jpg'
            new_id = module.add_user(username, password, temp_pic_path, pos['lng'], pos['lat'])
            session['username'] = username
            session['id'] = new_id
            session['lng'] = pos['lng']
            session['lat'] = pos['lat']
            print('已注册新用户：' + username)
            return redirect('/')
    return render_template('signup.html', signup_form=signup_form)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session.keys():
        return redirect('welcome')
    elif request.method == 'POST':
        data = (str(request.get_data(), encoding="UTF-8"))
        # 需要传回来的是的请求搜索的内容 如：{str:'麦当劳'}
        print(data)
    return render_template('index.html', username=session['username'])  # 用{{username}}代替右上角的用户名


@app.route('/group/new', methods=['GET', 'POST'])
def make_group():
    # session['id'] = 1  # 测试用
    # session['username'] = '111'  # 测试用
    # session['lng'] = 116.162  # 测试用
    # session['lat'] = 40.5355  # 测试用
    if 'username' not in session.keys():
        return redirect('login')
    elif request.method == 'GET':
        print('收到get')
        friend_list = module.search_friend_get_list(session['id'])
        print(friend_list)
        return render_template('make_group.html', result=json.dumps(friend_list))
        # friend_list格式：{id:{name:str,time:datetime,pic:str,loc_lng:float,loc_lat:float}
        # e.g.: {[ {"id":1, "loc_lng": 115.999, "time": 2, "pic": "/source/picture/icon/1.jpg", "name": "222", "loc_lat": 39.4825}, {"id":1, "loc_lng": 116.704, "time": 2, "pic": "/source/picture/icon/1.jpg", "name": "333", "loc_lat": 39.5186}]
    elif request.method == 'POST':
        print('收到post')
        data = json.loads(str(request.get_data(), encoding="UTF-8"))
        # 需要传回来的是勾选的id的dict,格式同friend_dict
        print(data)
        friend_loc = []
        friend_id = []
        for i in data:
            friend_loc.append([i['loc_lng'], i['loc_lat']])
            friend_id.append(int(i['id']))
        friend_loc.append([session['lng'], session['lat']])  # 计算总用时需要加上自己的坐标
        friend_id.append(session['id'])
        result = module.search_shop_get_id_list(friend_loc)  # 传回来的是shop_id的list 格式：[id1,id2,id3]
        session['shop_list'] = result
        session['people_list'] = friend_id
        print(session['people_list'])
        return redirect("location")
    return render_template('make_group.html')


@app.route('/location', methods=['GET', 'POST'])
def location():
    # session['username'] = '111'  # 测试用
    # session['shop_list'] = [12, 2, 3, 5]  # 测试用
    if request.method == 'GET':
        if 'username' in session.keys():
            result = module.search_shop_get_info_list(session['shop_list'])
            print(result)
            return render_template('location.html', result=json.dumps(result))
            # result格式：{'id':int, 'name': str, 'address': atr, 'evaluate': float, 'category': str,'pic': str, 'introduction': str}
        else:
            return redirect('login')
    if request.method == 'POST':
        if 'username' in session.keys():
            data = (str(request.get_data(), encoding="UTF-8"))
            # data = int(data)
            # 需要传回来的是商铺的id 如：{id:3}或{id:10}
            data = int(data.strip('"'))
            print(url_for('shop', id=data))
            return str(url_for('shop', id=data))
        else:
            return redirect('login')


@app.route('/shop', methods=['GET', 'POST'])
def shop():
    # session['username'] = '111'  # 测试用
    # session['people_list'] = [1, 2, 3]  # 测试用
    # session['shop_info'] = {'id': 5, 'name': '北京麦当劳潘家园餐厅', 'address': '北京市朝阳区劲松北路2号楼', 'evaluate': 5.0,
    #                         'category': '美食', 'pic': '/picture/0.jpg', 'introduction': '空空如也'}  # 测试用
    if request.method == 'GET':
        if 'username' in session.keys():
            get_id = request.args.get('id')
            result = module.search_shop_get_info_list([get_id])  # 只对选中的一个shop赋值
            print(result)
            session['shop_info'] = result  # 获取到id为get_id的value并赋值
            return render_template('shop.html', result=json.dumps(session['shop_info'][0]))
            # session['shop_info']格式：{'id':int, 'name': str, 'address': str, 'evaluate': float, 'category': str,'pic': str, 'introduction': str}
            # 如:{'name':'北京麦当劳潘家园餐厅','address':'北京市朝阳区劲松北路2号楼','evaluate':5.0,'category': '美食','pic': '/picture/0.jpg','introduction':'空空如也'}
        else:
            return redirect('login')
    if request.method == 'POST':  # 检测：如果需要显示定位信息，则发送POST请求
        if 'username' in session.keys():
            result_dic = {}
            x2, y2 = module.search_shop_get_loc(session['shop_info']['id'])
            for people_id in session['people_list']:
                x1, y1 = module.search_user_id_get_loc(people_id)
                count, destination = pos_generation.get_navi(x1, y1, x2, y2)
                result_dic[people_id] = [count, destination]
            print(result_dic)
            return json.dumps(result_dic)
            # result_dic格式: {user_id:['location','time(单位秒)'],user_id:['location','time(单位秒)']}
        else:
            return redirect('login')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    session.clear()
    if request.method == 'GET':
        if 'username' in session.keys():
            return redirect('/')
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=80)
