from django import template
import datetime

register = template.Library()

@register.filter
def format_datetime(datetime_str):
    # Parse the datetime string
    datetime_obj = datetime.datetime.fromisoformat(datetime_str)

    # Format the datetime as desired
    formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime