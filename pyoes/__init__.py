from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('header-footer', '/header-footer')
    config.add_route('grids', '/grids')
    config.add_route('beeldbank', '/beeldbank')
    config.add_route('beheersplannen', '/beheersplannen')
    config.add_route('actorenfront', '/actorenfront')
    config.add_route('detail-bedrijf', '/actorenfront/detail-bedrijf')
    config.add_route('detail-bedrijfv2', '/actorenfront/detail-bedrijfv2')
    config.add_route('detail', '/actorenfront/detail')
    config.add_route('actorenzoek', '/actorenzoek')
    config.add_route('actorenzoekdetail', '/actorenzoek/detail')
    config.add_route('beeldbank-detail', '/beeldbank-detail')
    config.add_route('beeldbank-zoeken', '/beeldbank-zoeken')
    config.add_route('inventaris', '/inventaris')
    config.add_route('inventaris-article', '/inventaris-article')
    config.add_route('inventaris-articleID', '/inventaris-articleID')
    config.add_route('inventaris-articleIDv2', '/inventaris-articleIDv2')
    config.add_route('inventaris-articleIDfull', '/inventaris-articleIDfull')
    config.add_route('inventaris-articleIDfullv2', '/inventaris-articleIDfullv2')
    config.add_route('inventaris-articleIDfullv3', '/inventaris-articleIDfullv3')
    config.add_route('inventaris-zoekoverzicht', '/inventaris-zoekoverzicht')
    config.add_route('icons', '/icons')
    config.add_route('blokken', '/blokken')
    config.add_route('typo', '/typo')
    config.add_route('navigation', '/navigation')
    config.add_route('colors', '/colors')
    config.add_route('elements', '/elements')
    config.add_route('images', '/images')
    config.add_route('article', '/article')
    config.add_route('article9-3', '/article9-3')
    config.add_route('geoportaal', '/geoportaal')
    config.add_route('pinpoints', '/pinpoints')

    includeme(config)

    config.scan('pyoes.views')
    return config.make_wsgi_app()


def includeme(config):
    
    config.add_static_view('pyoes_static', 'pyoes:static')
    config.scan('pyoes.static_views')

    return config
