# -*- coding: utf8 -*-

from __future__ import unicode_literals

from pyramid import testing

from pyoes import (
    includeme
)

class TestIncludeMe:

    def test_includeme(self):
        config = testing.setUp()
        includeme(config)
        del config
