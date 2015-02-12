# -*- coding: utf-8 -*-
'''
Contains utility methods.
'''


def set_attr_filter(target, key, value):
    '''
    Jinja2 filter that sets an attribute of an object.
    '''
    target[key] = value
    return target
