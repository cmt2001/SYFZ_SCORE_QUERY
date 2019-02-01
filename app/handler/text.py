from .import register_msg_type
from ..plugins import msg_keyword_resp

#注册文本消息由本函数处理
@register_msg_type('text')
def text_msg_handler(msg):
    for keyword in msg_keyword_resp:
        if keyword in msg.content:
            return msg_keyword_resp[keyword](msg)