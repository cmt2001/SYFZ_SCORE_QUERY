from ..vendor import msg_type_resp
from .. import flask_app
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
        response = flask_app.config['CANT_HANDLE_THIS_MESSAGE_TYPE']

    return response