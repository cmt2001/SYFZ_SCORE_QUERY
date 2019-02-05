# -*- coding: utf-8 -*-
from . import app
from flask import request
from .handler import wechat_response
from flask import render_template
from .models.firestore import db
import zlib,ast
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
@app.route('/score-report/<stu_id>/<time_stamp>', methods=['GET'])
def score(stu_id=None, time_stamp=None):
    #app.config['HOST_URL'] + f'/score-report/{params[1]}/{t}'
    doc = db.collection('score_data').document(stu_id).collection(time_stamp).document('data')
    res = doc.get().to_dict()[time_stamp]
    res = ast.literal_eval(bytes.decode(zlib.decompress(res)))
    return render_template('score.html',exam_info=res,update_time=time_stamp)

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