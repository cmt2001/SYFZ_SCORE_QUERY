# -*- coding: utf-8 -*-
from . import register_keyword
from .. import app
from sys import version_info
from .dep.score import invoke
if version_info.major != 3:
    raise RuntimeWarning(app.config['ERROR_RUNTIME_VERSION'] % u"python34")

@register_keyword('查成绩')
def query_score(msg):
    pass