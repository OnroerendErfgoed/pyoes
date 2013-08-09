# -*- coding: utf-8 -*-

from math import ceil


def set_attr_filter(target, key, value):
    '''
    Jinja2 filter om een attr in te stellen.
    '''
    target[key] = value
    return target
