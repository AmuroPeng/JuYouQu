# coding=utf8
# -*- coding:utf-8 -*-

from flask import Flask, render_template, flash, redirect, jsonify
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
            session['lng'], session['lat'] = module.search_user_get_loc(username)  # 并且更新了时间
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
    # return '哈罗 World~'
    return render_template('index.html')  # , username=session['username'] 目前不能加，因为没登录，没有username


@app.route('/group/new', methods=['GET', 'POST'])
def make_group():
    if request.method == 'GET':
        if 'username' in session.keys():
            friend_dict = module.search_friend_get_dict(session['id'])
            print(json.dumps(friend_dict))
            return render_template('test.html', result=json.dumps(friend_dict))  # 没把dict传到前端呢还
        else:
            return redirect('/login')

    elif request.method == 'POST':
        if 'username' in session.keys():
            data = json.loads(str(request.get_data(), encoding="UTF-8"))  # 需要传回来的是勾选的id的dict
            print(data)
            friend_loc = []
            if data == '':
                flash('请选择至少1个好友')
            else:
                for i, j in data.items():
                    print(j)
                    friend_loc.append([j['loc_lng'], j['loc_lat']])
                friend_loc.append([session['lng'], session['lat']])  # 计算总用时需要加上自己的坐标
                print(friend_loc)
                result = module.search_shop_get_list(friend_loc)  # 传回来的是shop_id的list
                session['shop_list'] = result
                return redirect('/location')
        else:
            return redirect('/login')


@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'GET':
        return render_template('location.html', result='none')


if __name__ == '__main__':
    app.run()
