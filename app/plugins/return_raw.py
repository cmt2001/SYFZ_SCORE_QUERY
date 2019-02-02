# -*- coding: utf-8 -*-
from .import register_keyword
from .. import flask_app
import wechatpy
@register_keyword("t")
def return_raw(msg):
    flask_app.logger.debug('message from %s handle by return_raw!' % msg.source)
    return wechatpy.replies.create_reply(msg.content,msg)