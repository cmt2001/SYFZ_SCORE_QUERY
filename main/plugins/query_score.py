# -*- coding: utf-8 -*-
from . import register_keyword
from .. import app
from sys import version_info
from .dep.score import get_meStudentScore
from ast import literal_eval
from wechatpy.replies import create_reply

if version_info.major != 3:
    raise RuntimeWarning(app.config['ERROR_RUNTIME_VERSION'] % u"python34")

def reply_articles(articles,msg):
    return create_reply(articles,msg)

@register_keyword('查成绩')
def query_score(msg):
    msg.content = (msg.content.replace('"', "").replace("“", "").replace(
            "”", "").replace("，",","))  # 首先处理一些无用数据 如空格 引号
    params = msg.content.split(" ")

    if len(params) == 2 and isinstance(literal_eval(params[1]),int):
        res = get_meStudentScore(params[1])
        if res['success']:
            return reply_articles([{
                'title': res['student_name']+'的成绩单',
                'url': app.config['HOST_URL'],
            }],msg)
        else:
            create_reply('获取失败，稍后再试')