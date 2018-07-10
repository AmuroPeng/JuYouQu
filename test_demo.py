# -*- coding:utf-8 -*-

# from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import json
import requests
loc='北京'
url = 'http://api.map.baidu.com/geocoder/v2/?address='+loc+'&output=json&ak=cSyuRk9MlTh1GV7dUSNxeM8kyg8Vu9MV'
json = requests.get(url).json()
# req = request.get(url,data=values,headers=headers)


print(url)
print(json)
# if __name__ == '__main__':
