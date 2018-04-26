# -*- coding: utf8 -*-
import unittest

from pyoes.utils import (
    set_attr_filter,
    datetime_format_filter,
    fuzzy_date_format_filter, _fuzzy_date_formatter)


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


class TestFuzzyDateFormatFilter(unittest.TestCase):
    def test_fuzzy_date_format_filter_default(self):
        from datetime import datetime
        d = datetime(2018, 4, 26, 20, 00)
        fd = fuzzy_date_format_filter(d)
        self.assertEqual('26-04-2018', fd)

    def test_fuzzy_date_format_filter_before_1900(self):
        from datetime import datetime
        d = datetime(1782, 4, 26, 20, 00)
        fd = fuzzy_date_format_filter(d)
        self.assertEqual('26-04-1782', fd)

    def test_fuzzy_date_format_filter_date(self):
        from datetime import date
        d = date(2018, 4, 26)
        fd = fuzzy_date_format_filter(d)
        self.assertEqual('26-04-2018', fd)

    def test_fuzzy_date_format_filter_custom_format(self):
        from datetime import datetime
        d = datetime(2018, 4, 26, 20, 00)
        fd = fuzzy_date_format_filter(d, '%m-%Y')
        self.assertEqual('04-2018', fd)
        d = datetime(2018, 4, 26, 20, 00)
        fd = fuzzy_date_format_filter(d, '%Y')
        self.assertEqual('2018', fd)

    def test_fuzzy_date_format_filter_default_parsed(self):
        fd = fuzzy_date_format_filter('26-04-2018 20:00')
        self.assertEqual('26-04-2018', fd)

    def test_fuzzy_date_format_filter_yearfirst(self):
        fd = fuzzy_date_format_filter('2018-04-26')
        self.assertEqual('26-04-2018', fd)

    def test_fuzzy_date_format_filter_yearfirst_daylast(self):
        fd = fuzzy_date_format_filter('2018-11-12')
        self.assertEqual('12-11-2018', fd)

    def test_fuzzy_date_format_filter_yearfirst_slash(self):
        fd = fuzzy_date_format_filter('2018/11/12')
        self.assertEqual('12-11-2018', fd)

    def test_fuzzy_date_format_filter_slash(self):
        fd = fuzzy_date_format_filter('12/11/12')
        self.assertEqual('12-11-2012', fd)

    def test_fuzzy_date_format_filter_none(self):
        fd = fuzzy_date_format_filter(None)
        self.assertEqual('', fd)

    def test_fuzzy_date_formatter_default(self):
        from datetime import datetime
        d = datetime(2018, 4, 26, 20, 00)
        fd = _fuzzy_date_formatter(d)
        self.assertEqual('26-04-2018', fd)

    def test_fuzzy_date_formatter_day_month_year(self):
        from datetime import datetime
        d = datetime(2018, 4, 26, 20, 00)
        fd = _fuzzy_date_formatter(d, '%d-%m-%Y')
        self.assertEqual('26-04-2018', fd)

    def test_fuzzy_date_formatter_month_year(self):
        from datetime import datetime
        d = datetime(2018, 4, 26, 20, 00)
        fd = _fuzzy_date_formatter(d, '%m-%Y')
        self.assertEqual('04-2018', fd)

    def test_fuzzy_date_formatter_year(self):
        from datetime import datetime
        d = datetime(2018, 4, 26, 20, 00)
        fd = _fuzzy_date_formatter(d, '%Y')
        self.assertEqual('2018', fd)

    def test_fuzzy_date_formatter_not_defined_formar(self):
        from datetime import datetime
        d = datetime(2018, 4, 26, 20, 00)
        fd = _fuzzy_date_formatter(d, '%Y-%d-%m')
        self.assertEqual('26-04-2018', fd)
