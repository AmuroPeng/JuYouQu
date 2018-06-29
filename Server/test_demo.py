# -*- coding:utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


# 定义路由
@app.route('/', methods=['GET', 'POST'])
def index():
    url_str = 'www.baidu.com'

    my_list = [1, 3, 5, 7, 9]

    my_dict = {
        'name':'name',
        'name2': url_str
    }

    # return '哈罗 World~'
    return render_template('index.html', url_str=url_str, my_list=my_list,my_dict=my_dict)


@app.route('/orders/<int:order_id>', methods=['GET', 'POST'])
def get_order_id(order_id):
    return 'order_id %s' % order_id


if __name__ == '__main__':
    app.run()
