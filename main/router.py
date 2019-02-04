# -*- coding: utf-8 -*-
from . import app
from flask import request
from .handler import wechat_response
from flask import render_template
#从plugin目录调用所有注册了的插件
from .flask_wechatpy import Wechat, wechat_required, oauth
#路由文件
#访问不同网址由本文件处理

#微信公众号调用接口
@app.route('/', methods=['GET','POST'])
@wechat_required
def handle_wechat_requst():
    msg = request.wechat_msg
    return wechat_response(msg)

@app.route('/wechat')
def index():
    return 'hello'

@app.route('/test')
def test():
    exam_info = {
        'name' :'student name',
        'all_exam' :[
            {'name': '第一次考试',
                'data': [
                    {
                        'name': 'shuxue',
                        'score': '96',
                    },
                    {
                        'name': 'yuwen',
                        'score': '33',
                    },
                    {
                        'name': 'yingyu',
                        'score': '96',
                    },
                    ]
            },
            {'name': '第二次考试',
                'data': [
                    {
                        'name': 'shuxue',
                        'score': '96',
                    },
                    {
                        'name': 'yuwen',
                        'score': '33',
                    },
                    {
                        'name': 'yingyu',
                        'score': '96',
                    },
                    ]
            },
            {'name': '第三次考试',
                'data': [
                    {
                        'name': 'shuxue',
                        'score': '96',
                    },
                    {
                        'name': 'yuwen',
                        'score': '33',
                    },
                    {
                        'name': 'yingyu',
                        'score': '96',
                    },
                    ]
            }
        ]
    }
    real_name = exam_info['name']
    return render_template('score.html',exam_info=exam_info,real_name=real_name)