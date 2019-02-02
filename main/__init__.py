# -*- coding: utf-8 -*-
from flask import Flask
flask_app = Flask(__name__, instance_relative_config=True)
# 根目录下面的config
flask_app.config.from_object('config') 
# instance下面的config
flask_app.config.from_pyfile('config.py')
# 加载flask路由配置
from .import router