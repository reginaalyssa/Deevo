from django import template

register = template.Library()

@register.filter
def remove_backslash(string):
    return string.replace("\\", "")