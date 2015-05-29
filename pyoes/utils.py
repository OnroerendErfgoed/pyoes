# -*- coding: utf-8 -*-
'''
Contains some extra filters for Jinja2.

To use these, they need to be registered in your pyramid config.
'''
from dateutil import tz, parser

def set_attr_filter(target, key, value):
    '''
    Jinja2 filter that sets an attribute of an object.
    '''
    target[key] = value
    return target

def datetime_format_filter(value, format='%d-%m-%Y %H:%M'):
    """
    Jinja 2 filter to print a datetime object in a template.

    :param value: Eiter a :class:`datetime.datetime` or a string that can be \
        parsed by :class:`dateutil.parser`. In case of ambiguity between the \
        day and the month, the parser will assume the day precedes the month \
        (ie. European way)
    :param format: The format to print the date in.
    :return: The formatted date, eg. `07-09-2014 20:00`.
    """
    try:
        return value.strftime(format)
    except AttributeError:
        date = parser.parse(value, dayfirst=True)
        return date.strftime(format)
