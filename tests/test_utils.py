# -*- coding: utf8 -*-

from pyoes.utils import (
    set_attr_filter,
    datetime_format_filter
    )

class TestSetAttr:

    def test_set_attr_filter(self):
        d = {}
        d2 = set_attr_filter(d, 'pagina', 1)
        assert d2 == {'pagina': 1}

    def test_set_attr_filter_overwrites(self):
        d = {'pagina': 1}
        d2 = set_attr_filter(d, 'pagina', 10)
        assert d2 == {'pagina': 10}

class TestDatetimeFormatFilter:

    def test_datetime_format_filter_default(self):
        from datetime import datetime
        d = datetime(2014, 9, 7, 20, 00)
        fd = datetime_format_filter(d)
        assert fd == '07-09-2014 20:00'

    def test_datetime_format_filter_custom_format(self):
        from datetime import datetime
        d = datetime(2014, 9, 7, 20, 00)
        fd = datetime_format_filter(d, '%d-%m-%Y')
        assert fd == '07-09-2014'

    def test_datetime_format_filter_default_parsed(self):
        fd = datetime_format_filter('07-09-2014 20:00')
        assert fd == '07-09-2014 20:00'
