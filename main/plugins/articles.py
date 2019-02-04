# -*- coding: utf-8 -*-
from . import register_keyword
from wechatpy.replies import create_reply

def reply_articles(msg,articles):
    return create_reply(articles,msg)