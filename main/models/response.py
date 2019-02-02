# -*- coding: utf-8 -*-
from ..vendor import msg_type_resp
from .. import app
from wechatpy.replies import create_reply
def wechat_response(message):
    '''
    微信消息处理函数
    :data 从微信服务器传来的数据
    '''
    response = '未知错误'
    try:
        get_resp_handler = msg_type_resp[message.type]
        response = get_resp_handler(message)
    except KeyError:
        content = app.config['CANT_HANDLE_THIS_MESSAGE_TYPE']
        response = create_reply(content,message)

    return response