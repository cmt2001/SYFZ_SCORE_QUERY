from .handler_list import all_handler
from .. import flask_app
import importlib
msg_type_resp = {}

def register_msg_type(msg_type):
    """
    储存微信消息类型所对应函数（方法）的装饰器
    """
    def decorator(func):
        msg_type_resp[msg_type] = func
        return func
    return decorator

for handler in all_handler:
    try:
        importlib.import_module('.'+handler, package=__package__)
    except ImportError:
        flask_app.logger.warning(flask_app.config['ERROR_IMPORT_HANDLER'] % handler)
