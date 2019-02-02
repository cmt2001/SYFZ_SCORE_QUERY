# -*- coding: utf-8 -*-
from .plugins_list import all_plugin
from ..import flask_app
import importlib
msg_keyword_resp = {}

def register_keyword(keyword):
    """
    储存消息关键词所对应函数（方法）的装饰器
    """
    def decorator(func):
        msg_keyword_resp[keyword] = func
        return func
    return decorator

for plugin in all_plugin:
    try:
        importlib.import_module('.'+plugin, package=__package__)
    except ImportError:
        flask_app.logger.warning(flask_app.config['ERROR_IMPORT_PLUGIN'] % plugin)