import unittest

from pyramid import testing

from pyramid.response import (
    FileResponse
)

class StaticViewTests(unittest.TestCase):

    def _get_static_view(self, request):
        from pyoes.static_views import StaticView
        return StaticView(request)

    def test_robotstxt(self):
        request = testing.DummyRequest()
        sv = self._get_static_view(request)
        res = sv.robotstxt()
        self.assertIsInstance(res, FileResponse)
        self.assertEqual('text/plain', res.content_type)

    def test_faviconico(self):
        request = testing.DummyRequest()
        sv = self._get_static_view(request)
        res = sv.faviconico()
        self.assertIsInstance(res, FileResponse)
        assert res.content_type in ['image/x-icon', 'image/vnd.microsoft.icon']
