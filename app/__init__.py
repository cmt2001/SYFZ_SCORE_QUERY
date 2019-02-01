#微信消息处理框架导入
from flask_wechatpy import Wechat, wechat_required, oauth

#从plugin目录调用所有注册了的插件
from flask import Flask
flask_app = Flask(__name__, instance_relative_config=True)
flask_app.config.from_object('config') #根目录下面的config
flask_app.config.from_pyfile('config.py') #instance下面的config
from .import router