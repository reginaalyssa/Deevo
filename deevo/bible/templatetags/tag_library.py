from django import template

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)

@register.filter
def addstr(arg1, arg2):
    return str(arg1) + str(arg2)