# -*- coding:utf-8 -*-

from flask import Flask, render_template, flash, redirect, jsonify
from flask import request, session
import form
import module
import json
import logging
import pos_generation
from sqlalchemy.orm import class_mapper

app = Flask(__name__)
app.secret_key = '111'
# 全局变量
friend_dict = {}  # 好友列表（包含位置）


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = form.LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if password == module.search_user_get_password(username):
            print('密码正确')
            session['lng'], session['lat'] = module.search_user_get_loc(username)  # 并且更新了时间
            session['username'] = username
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
            print('已注册新用户：' + username)
            return redirect('/')
    return render_template('signup.html', signup_form=signup_form)


@app.route('/', methods=['GET', 'POST'])
def index():
    # return '哈罗 World~'
    return render_template('index.html')  # , username=session['username'] 目前不能加，因为没登录，没有username


@app.route('/group/new', methods=['GET', 'POST'])
def make_group(self):
    if request.method == 'GET':
        if 'username' in session.keys():
            self.friend_dict = module.search_friend_get_dict(session['username'])
            return render_template('make_group.html', result=jsonify(self.friend_dict))  # 没把dict传到前端呢还
        else:
            return redirect('/login')

    elif request.method == 'POST':
        self.friend_dict = {}  # 用于每次重新添加列表时清空上次记录
        data = json.loads(str(request.get_data(), encoding="UTF-8"))
        # 差算法


if __name__ == '__main__':
    app.run()
