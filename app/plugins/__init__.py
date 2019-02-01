__all__ = ['check_score','return_raw']
msg_keyword_resp = {}
def register_keyword(keyword):
    """
    储存消息关键词所对应函数（方法）的装饰器
    """
    def decorator(func):
        msg_keyword_resp[keyword] = func
        return func
    return decorator