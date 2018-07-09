# -*- coding:utf-8 -*-

import flask
import mysql
import pymysql
import mysql.connector
from flask import Flask, render_template, flash, redirect, url_for
from flask import request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import form
import module
import logging
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

app = Flask(__name__)
app.secret_key = '111'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            session['username'] = request.form['username']
            return redirect('/')
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
            module.add_user(username,password)
            logging.info('已注册新用户：' + username)
            return redirect('/')
    return render_template('signup.html')


# 定义路由
@app.route('/', methods=['GET', 'POST'])
def index():
    # return '哈罗 World~'
    return render_template('index.html')  # , username=session['username']


@app.route('/location', methods=['GET', 'POST'])
def location():
    return render_template('location.html')


if __name__ == '__main__':
    app.run()
