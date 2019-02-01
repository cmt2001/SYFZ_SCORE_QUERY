from .import register_keyword

@register_keyword("")
def return_raw(msg):
    return msg.content