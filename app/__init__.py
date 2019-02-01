#从plugin目录调用所有注册了的插件
from flask import Flask
flask_app = Flask(__name__, instance_relative_config=True)
flask_app.config.from_object('config') #根目录下面的config
flask_app.config.from_pyfile('config.py') #instance下面的config
#加载flask路由配置
from .import router