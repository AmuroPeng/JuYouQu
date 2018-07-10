# -*- coding:utf-8 -*-

from flask import Flask, render_template, flash, redirect
import json
import requests


def get_loc(loc):
    url = 'http://api.map.baidu.com/geocoder/v2/?address=' + loc + '&output=json&ak=cSyuRk9MlTh1GV7dUSNxeM8kyg8Vu9MV'
    get_result = requests.get(url).json()
    if get_result['status'] == 0:  # 服务器错误
        json_result = get_result['result']
        if json_result['level'] == 'UNKNOWN':
            return "位置信息有误无法识别，请重新输入"
        else:
            return json_result['location']
    else:
        return "百度服务器错误暂时无法定位"


if __name__ == '__main__':
    result = get_loc('北京')
    print(result)
    if type(result) == dict:
        print(1)
    else:print(2)
