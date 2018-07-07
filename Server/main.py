# -*- coding:utf-8 -*-

import sys
from flask import Flask, render_template
import mysql
import pymysql
import mysql.connector
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import form

app = Flask(__name__)
app.secret_key = '111'


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = form.LoginForm()
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([username, password, password2]):
            flash("参数不完整")
        elif password != password2:
            flash('密码不一致')
        else:
            return render_template('demo.html', form=login_form)
    return render_template('login.html', form=login_form)


# 定义路由
@app.route('/', methods=['GET', 'POST'])
def index():

    # return '哈罗 World~'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
