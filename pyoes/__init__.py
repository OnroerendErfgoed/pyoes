# -*- coding: utf-8 -*-

from pyramid.config import Configurator


def main(global_config, **settings):  # pragma: no cover
    """
    Returns a pyramid application that can help demo the style.
    """
    config = Configurator(settings=settings)
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("burgerprofiel", "/burgerprofiel")
    config.add_route("burgerprofiel2", "/burgerprofiel2")
    config.add_route("headerlinks", "/headerlinks")
    config.add_route("navigation", "/navigation")
    config.add_route("401", "/401")
    config.add_route("403", "/403")
    config.add_route("404", "/404")
    config.add_route("500", "/500")

    includeme(config)

    config.scan("pyoes.views")
    return config.make_wsgi_app()


def includeme(config):
    """
    Include pyoes in a pyramid application.

    :param pyramid.config.Configurator config:
    """

    config.add_static_view("pyoes_static", "pyoes:static")
    config.scan("pyoes.static_views")

    return config
