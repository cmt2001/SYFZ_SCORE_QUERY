from . import flask_app
from flask import request
from .models.response import wechat_response
#路由文件
#访问不同网址由本文件处理

#微信公众号调用接口
@flask_app.route('/wechat', methods=['GET','POST'])
def handle_wechat_requst():
    if request.method == 'GET':
        return wechat_response(request.args)
    return 'hello'

