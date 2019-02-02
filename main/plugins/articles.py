# -*- coding: utf-8 -*-
from . import register_keyword
from wechatpy.replies import ArticlesReply
from wechatpy.replies import create_reply

@register_keyword(u'图文')
def reply_articles(msg):
    articles = [
        {
            'title': 'this a test',
            'description': 'this is a description',
            'url': 'localhost',
        },
        {
        'title': 'this a test2',
            'description': 'this is a description2',
            'url': 'localhost2',
        },
    ]
    return create_reply(articles,msg)

'''
def reply_articles(msg):
    return make_articles(
        msg, {
            'title': 'this a test',
            'description': 'this is a description',
            'url': 'localhost',
        })
'''

def make_articles(msg, articles):
    '''
    向用户返回图文消息
    :msg 经过解析的用户dict
    :articles 文章list
    '''
    reply = ArticlesReply(message=msg)

    if isinstance(articles, list):
        for article in articles:
            reply.add_article(article)
    elif isinstance(articles, dict):
        reply.add_article(articles)
    else:
        from .. import app
        app.logger.warning(
            'make_articles cant handle this message!\n%s' % articles)

    return reply