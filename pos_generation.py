# -*- coding:utf-8 -*-

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


def get_navi(origin_lng, origin_lat, destination_lng, destination_lat):
    origin_str = str(origin_lat) + ',' + str(origin_lng)
    destination_str = str(destination_lat) + ',' + str(destination_lng)
    url = 'http://api.map.baidu.com/direction/v2/transit?origin=' + origin_str + '&destination=' + destination_str + '&ak=erY9nr7Yf7zh7qc0KbTLfaOd'
    get_result = requests.get(url).json()
    if get_result['status'] == 0:  # 服务器错误
        json_result = get_result['result']
        json_routes = json_result['routes']
        json_steps = json_routes[0]['steps']
        json_duration = json_routes[0]['duration']
        routes = ''
        for json_step in json_steps:
            json_instructions = json_step[0]['instructions']
            routes = routes + " " + json_instructions
        return routes, json_duration  # routes是行程规划,json_duration是用时（秒）
    else:
        print("百度服务器错误暂时无法定位")
        return '百度服务器错误暂时无法定位', 99999


if __name__ == '__main__':
    print(get_navi(116.396, 39.93, 116.531, 39.54))

# if __name__ == '__main__':
#     result = get_loc('北京')
#     print(result)
