from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_date(value, format_string):
    return value.strftime(format_string)