# -*- coding: utf8 -*-

import unittest

from pyoes.utils import (
    set_attr_filter
    )

class UtilTests(unittest.TestCase):

    def test_set_attr_filter(self):
        d = {}
        d2 = set_attr_filter(d, 'pagina', 1)
        self.assertEquals({'pagina': 1}, d2)

    def test_set_attr_filter_overwrites(self):
        d = {'pagina': 1}
        d2 = set_attr_filter(d, 'pagina', 10)
        self.assertEquals({'pagina': 10}, d2)
