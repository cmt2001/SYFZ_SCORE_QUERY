# -*- coding: utf-8 -*-
from . import register_keyword
from .. import app
from sys import version_info
from .dep.score import get_meStudentScore
from ast import literal_eval
from wechatpy.replies import create_reply
from ..models.firestore import db
import time
import zlib
from ...test import res
if version_info.major != 3:
    raise RuntimeWarning(app.config['ERROR_RUNTIME_VERSION'] % u"python34")


def reply_articles(articles, msg):
    return create_reply(articles, msg)


@register_keyword('查成绩')
def query_score(msg):
    msg.content = (msg.content.replace('"', "").replace("“", "").replace(
        "”", "").replace("，", ","))  # 首先处理一些无用数据 如空格 引号
    params = msg.content.split(" ")

    try:
        int(params[1])
    except:
        return create_reply('输入内容不合法',msg)
    else:
        if len(params) == 2:
            # 查询
            res = get_meStudentScore(params[1])
            # 保存到firestore
            t = time.time()
            t = str(int(t))
            doc_ref = db.collection('score_data').document(
                params[1]).collection(t).document('data')
            res_comp = zlib.compress(str.encode(str(res)))
            doc_ref.set({
                t: res_comp,
            })
            # 查询成功
            if res['success']:
                return reply_articles([{
                    'title':
                    res['student_name'] + '的成绩单',
                    'url':
                    app.config['HOST_URL'] + f'/score-report/{params[1]}/{t}'
                }], msg)
            else:
                return create_reply('获取失败，稍后再试',msg)