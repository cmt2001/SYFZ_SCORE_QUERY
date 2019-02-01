from . import flask_app
from flask import request
from .models.response import wechat_response
#从plugin目录调用所有注册了的插件
from .flask_wechatpy import Wechat, wechat_required, oauth
#路由文件
#访问不同网址由本文件处理

#微信公众号调用接口
@flask_app.route('/wechat', methods=['GET','POST'])
@wechat_required
def handle_wechat_requst():
    msg = request.wechat_msg
    return wechat_response(msg)



