# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)

app.secret_key = '111'


class LoginForm(FlaskForm):
    username = StringField('用户名')
    password = PasswordField('密码')
    password2 = PasswordField('确认密码')
    submit = SubmitField('提交')


# @app.route('/form', methods=['GET', 'POST'])
# def login():
#     login_form = LoginForm()
#     return render_template('index.html', form=login_form)


# 定义路由
@app.route('/', methods=['GET', 'POST'])
def index():
    url_str = 'www.baidu.com'

    my_list = [1, 3, 5, 7, 9]

    my_dict = {
        'name': 'name',
        'name2': url_str
    }

    login_form = LoginForm()

    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if not all([username, password, password2]):
        flash("参数不完整")
    elif password != password2:
        flash('密码不一致')
    else:
        return 'success'

    print(username)
    # return '哈罗 World~'
    return render_template('index.html', url_str=url_str, my_list=my_list, my_dict=my_dict,form=login_form)


@app.route('/orders/<int:order_id>', methods=['GET', 'POST'])
def get_order_id(order_id):
    return 'order_id %s' % order_id


if __name__ == '__main__':
    app.run()
