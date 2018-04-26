# -*- coding: utf-8 -*-
"""
Contains some extra filters for Jinja2.

To use these, they need to be registered in your pyramid config.
"""
from dateutil import parser


def set_attr_filter(target, key, value):
    """
    Jinja2 filter that sets an attribute of an object.
    """
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
    if value:
        try:
            return value.strftime(format)
        except AttributeError:
            if value[0:4].find('-') == -1 and value[0:4].find('/') == -1:
                date = parser.parse(value, yearfirst=True, dayfirst=False)
            else:
                date = parser.parse(value, dayfirst=True)
            return date.strftime(format)
    else:
        return ''


def fuzzy_date_format_filter(value, format='%d-%m-%Y'):
    """
    Jinja 2 filter to print a fuzzy date object in a template.

    :param value: Eiter a :class:`datetime.datetime` or a string that can be \
        parsed by :class:`dateutil.parser`. In case of ambiguity between the \
        day and the month, the parser will assume the day precedes the month \
        (ie. European way)
    :param format: The format to print the date in.
    :return: The formatted date, eg. `07-09-2014 20:00`.
    """
    if value:
        try:
            return _fuzzy_date_formatter(value, format)
        except AttributeError:
            if value[0:4].find('-') == -1 and value[0:4].find('/') == -1:
                date = parser.parse(value, yearfirst=True, dayfirst=False)
            else:
                date = parser.parse(value, dayfirst=True)
            return _fuzzy_date_formatter(date, format)
    else:
        return ''


def _fuzzy_date_formatter(date, format='%d-%m-%Y'):
    """
    Dateconverter to convert date or datetime objects to strings in a specific format

    Implemented because of the problems of datetime.strftime method with years before 1900
    :param date:
    :param format: The format to print the date in. (must be a predefined format)
                    '%d-%m-%Y' or '%m-%Y' or '%Y'
    :return: The formatted date, eg. `07-09-2014`
    """
    if format == '%d-%m-%Y':
        return '{0.day:02d}-{0.month:02d}-{0.year:4d}'.format(date)
    elif format == '%m-%Y':
        return '{0.month:02d}-{0.year:4d}'.format(date)
    elif format == '%Y':
        return '{0.year:4d}'.format(date)
    else:
        # Default
        return '{0.day:02d}-{0.month:02d}-{0.year:4d}'.format(date)
