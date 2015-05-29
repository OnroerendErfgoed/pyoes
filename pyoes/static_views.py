from pyramid.view import (
    view_config
)

import os

from pyramid.response import (
    FileResponse
)

class StaticView(object):
    '''
    Views voor aan de root gebonden static files.
    '''
    def __init__(self, request):
        self.request = request
        self.here = os.path.dirname(__file__)

    @view_config(name='favicon.ico')
    def faviconico(self):
        '''
        View om een statische favicon.ico te kunnen serveren
        '''
        icon = os.path.join(self.here, 'static', 'favicon.ico')
        return FileResponse(icon, request=self.request)

    @view_config(name='robots.txt')
    def robotstxt(self):
        '''
        View om een statische robots.txt te kunnen serveren
        '''
        icon = os.path.join(self.here, 'static', 'robots.txt')
        return FileResponse(icon, request=self.request)
