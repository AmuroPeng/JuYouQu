# -*- coding:utf-8 -*-

from flask import Flask, render_template, flash, redirect
from flask import request, session
import form
import module
import logging
import pos_generation

app = Flask(__name__)
app.secret_key = '111'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            session['username'] = request.form['username']
            return redirect('/')
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


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
            module.add_user(username, password, pos['lat'], pos['lng'])
            logging.info('已注册新用户：' + username)
            return redirect('/')
    return render_template('signup.html', signup_form=signup_form)


@app.route('/', methods=['GET', 'POST'])
def index():
    # return '哈罗 World~'
    return render_template('index.html')  # , username=session['username']


@app.route('/location', methods=['GET', 'POST'])
def location():
    return render_template('location.html')


if __name__ == '__main__':
    app.run()
