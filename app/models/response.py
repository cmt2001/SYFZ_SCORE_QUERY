from ..vendor import msg_type_resp
from .. import flask_app
def wechat_response(data):
    '''
    global message, openid, wechat
    wechat = init_wechat_sdk()
    wechat.parse_data(data)
    message = wechat.get_message()
    openid = message.source
    '''
    response = '未知错误'
    message = data
    message.content = message['content']
    message.type = message['type']
    message.content = message.content.replace(u'　', ' ')
    message.content = message.content.lstrip()
    try:
        get_resp_handler = msg_type_resp[message.type]
        response = get_resp_handler(message)
    except KeyError:
        response = flask_app.config['CANT_HANDLE_THIS_MESSAGE_TYPE']

    return response