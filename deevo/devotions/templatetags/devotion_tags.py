from django import template

register = template.Library()

@register.filter
def limit_char_140(string):
    if len(string) > 140:
        return string[:140] + "..."
    return string