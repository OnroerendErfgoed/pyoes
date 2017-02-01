# -*- coding: utf8 -*-
import unittest

from pyoes.utils import (
    set_attr_filter,
    datetime_format_filter
)


class TestSetAttr(unittest.TestCase):
    def test_set_attr_filter(self):
        d = {}
        d2 = set_attr_filter(d, 'pagina', 1)
        self.assertEqual({'pagina': 1}, d2)

    def test_set_attr_filter_overwrites(self):
        d = {'pagina': 1}
        d2 = set_attr_filter(d, 'pagina', 10)
        self.assertEqual({'pagina': 10}, d2)


class TestDatetimeFormatFilter(unittest.TestCase):
    def test_datetime_format_filter_default(self):
        from datetime import datetime
        d = datetime(2014, 9, 7, 20, 00)
        fd = datetime_format_filter(d)
        self.assertEqual('07-09-2014 20:00', fd)

    def test_datetime_format_filter_date(self):
        from datetime import date
        d = date(2014, 9, 7)
        fd = datetime_format_filter(d, format='%d-%m-%Y')
        self.assertEqual('07-09-2014', fd)

    def test_datetime_format_filter_custom_format(self):
        from datetime import datetime
        d = datetime(2014, 9, 7, 20, 00)
        fd = datetime_format_filter(d, '%d-%m-%Y')
        self.assertEqual('07-09-2014', fd)

    def test_datetime_format_filter_default_parsed(self):
        fd = datetime_format_filter('07-09-2014 20:00')
        self.assertEqual('07-09-2014 20:00', fd)

    def test_datetime_format_filter_yearfirst(self):
        fd = datetime_format_filter('2017-01-26')
        self.assertEqual('26-01-2017 00:00', fd)

    def test_datetime_format_filter_yearfirst_daylast(self):
        fd = datetime_format_filter('2017-11-12')
        self.assertEqual('12-11-2017 00:00', fd)

    def test_datetime_format_filter_yearfirst_slash(self):
        fd = datetime_format_filter('2017/11/12')
        self.assertEqual('12-11-2017 00:00', fd)

    def test_datetime_format_filter_slash(self):
        fd = datetime_format_filter('12/11/12')
        self.assertEqual('12-11-2012 00:00', fd)

    def test_datetime_format_filter_none(self):
        fd = datetime_format_filter(None)
        self.assertEqual('', fd)
