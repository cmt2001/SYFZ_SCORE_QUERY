# -*- coding: utf-8 -*-
from wechatpy.replies import create_reply
from .handler_list import all_handler
from .. import app
import importlib
msg_type_resp = {}

def register_msg_type(msg_type):
    """
    储存微信消息类型所对应函数（方法）的装饰器
    """
    def decorator(func):
        msg_type_resp[msg_type] = func
        return func
    return decorator

for handler in all_handler:
    try:
        importlib.import_module('.'+handler, package=__package__)
    except ImportError:
        app.logger.warning(app.config['ERROR_IMPORT_HANDLER'] % handler)


def wechat_response(message):
    '''
    微信消息处理函数
    :message 从微信服务器传来的数据
    '''
    response = '未知错误'
    try:
        get_resp_handler = msg_type_resp[message.type]
        response = get_resp_handler(message)
    except Exception as e:
        content = app.config['CANT_HANDLE_THIS_MESSAGE_TYPE']
        response = create_reply(content,message)
        app.logger.warning(e)

    return response