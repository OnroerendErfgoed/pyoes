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
    config.add_route('beeldbank-detail', '/beeldbank-detail')
    config.add_route('inventaris', '/inventaris')

    includeme(config)

    config.scan('pyoes.views')
    return config.make_wsgi_app()


def includeme(config):
    
    config.add_static_view('pyoes_static', 'pyoes:static')
    config.scan('pyoes.static_views')

    return config
