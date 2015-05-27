# -*- coding: utf-8 -*-
'''
Contains utility methods.
'''
from dateutil import tz, parser

def set_attr_filter(target, key, value):
    '''
    Jinja2 filter that sets an attribute of an object.
    '''
    target[key] = value
    return target

def datetime_format_filter(value, formatation='%d-%m-%Y %H:%M'):    #pragma NO COVER
    """
    Jinja2 filter om een datetime object af te drukken in een template.
    Deze functie wordt momenteel nog niet gebruikt binnen adviezen

    :param value:
    :param formatation:
    :return:
    """
    try:
        return value.strftime(formatation)
    except AttributeError:
        date = parser.parse(value)
        return date.strftime(formatation)