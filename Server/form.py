# -*- coding:utf-8 -*-

from flask import Flask, render_template
import mysql
import pymysql
import mysql.connector
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    username = StringField('用户名')
    password = PasswordField('密码')
    password2 = PasswordField('确认密码')
    submit = SubmitField('提交')