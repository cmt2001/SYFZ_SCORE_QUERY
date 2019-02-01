from .import register_msg_type
from ..plugins import msg_keyword_resp
import re
from flask import current_app as app
#TODO 添加用户状态

#注册文本消息由本函数处理
@register_msg_type('text')
def text_msg_handler(message):
    """文本类型回复"""

    # 替换全角空格为半角空格
    message.content = message.content.replace(u'　', ' ')
    # 清除行首空格
    message.content = message.content.lstrip()

    # 匹配指令(关键词)
    keyword_match = False
    for keyword in msg_keyword_resp:
        if re.match(keyword, message.content):
            # 指令匹配后，设置默认状态
            # set_user_state(openid, 'default')
            response = msg_keyword_resp[keyword]()
            keyword_match = True
            break
    
    if not keyword_match:
        # TODO：匹配状态
        #state = get_user_state(openid)
        # 关键词、状态都不匹配，缺省回复
        #if state == 'default' or not state:
        #    response = command_not_found()
        #else:
        #    response = state_commands[state]()
        response = command_not_found()

    return response


#下面是固定指令 不绑定任何关键词/状态.需要主动调用
def command_not_found():
    """非关键词回复"""
    content = app.config['COMMAND_NOT_FOUND_TEXT'] + app.config['HELP_TEXT']
    return content