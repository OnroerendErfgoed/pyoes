"""
Pyramid integration: ``config.include("pyoes")`` serves the pyoes static files
and makes the ``pyoes`` template context available in every rendered template.
"""

from pyramid.config import Configurator
from pyramid.events import BeforeRender


class PyramidContext:
    """
    Lazy :class:`pyoes.context.PyoesContext` for pyramid; it is added to every
    render (json included) and ``request.user`` can be expensive.
    """

    def __init__(self, request):
        self.request = request

    def _setting(self, key):
        return self.request.registry.settings.get(key)

    def route_path(self, name, *elements, **kw):
        return self.request.route_path(name, *elements, **kw)

    def static_path(self, spec, **kw):
        return self.request.static_path(spec, **kw)

    @property
    def plausible_domain_hash(self):
        return self._setting("plausible.domain_hash")

    @property
    def burgerprofiel_header_id(self):
        return self._setting("burgerprofiel.header_id")

    @property
    def burgerprofiel_footer_id(self):
        return self._setting("burgerprofiel.footer_id")

    @property
    def banner(self):
        return self._setting("pyoes.banner")

    @property
    def banner_detail(self):
        return self._setting("pyoes.banner.detail")

    @property
    def authenticated_userid(self):
        return self.request.authenticated_userid

    @property
    def user(self):
        return getattr(self.request, "user", None)

    @property
    def home_url(self):
        return self.route_path("home")


def add_pyoes_context(event):
    request = event.get("request")
    if request is not None and "pyoes" not in event:
        event["pyoes"] = PyramidContext(request)


def includeme(config):
    """
    Include pyoes in a pyramid application.

    :param pyramid.config.Configurator config:
    """

    config.add_static_view("pyoes_static", "pyoes:static")
    config.scan("pyoes.static_views")
    config.add_subscriber(add_pyoes_context, BeforeRender)

    return config


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
    config.add_route("grids", "/grids")
    config.add_route("beeldbank", "/beeldbank")
    config.add_route("beheersplannen", "/beheersplannen")
    config.add_route("beheersplannenres", "/beheersplannen/result")
    config.add_route("actorenfront", "/actorenfront")
    config.add_route("detail-bedrijf", "/actorenfront/detail-bedrijf")
    config.add_route("detail-bedrijfv2", "/actorenfront/detail-bedrijfv2")
    config.add_route("detail", "/actorenfront/detail")
    config.add_route("actorenzoek", "/actorenzoek")
    config.add_route("actorenzoekdetail", "/actorenzoek/detail")
    config.add_route("beeldbank-detail", "/beeldbank-detail")
    config.add_route("beeldbank-zoeken", "/beeldbank-zoeken")
    config.add_route("besluitendatabank", "/besluitendatabank")
    config.add_route("inventaris", "/inventaris")
    config.add_route("inventaris-article", "/inventaris-article")
    config.add_route("inventaris-articleID", "/inventaris-articleID")
    config.add_route("inventaris-articleIDv2", "/inventaris-articleIDv2")
    config.add_route("inventaris-articleIDfull", "/inventaris-articleIDfull")
    config.add_route("inventaris-articleIDfullv2", "/inventaris-articleIDfullv2")
    config.add_route("inventaris-articleIDfullv3", "/inventaris-articleIDfullv3")
    config.add_route("inventaris-zoekoverzicht", "/inventaris-zoekoverzicht")
    config.add_route("postregistratie", "/postregistratie")
    config.add_route("postreg-aanmaken", "/postregistratie/aanmaken")
    config.add_route("icons", "/icons")
    config.add_route("blokken", "/blokken")
    config.add_route("typo", "/typo")
    config.add_route("navigation", "/navigation")
    config.add_route("colors", "/colors")
    config.add_route("elements", "/elements")
    config.add_route("images", "/images")
    config.add_route("article", "/article")
    config.add_route("article9-3", "/article9-3")
    config.add_route("geoportaal", "/geoportaal")
    config.add_route("pinpoints", "/pinpoints")
    config.add_route("401", "/401")
    config.add_route("403", "/403")
    config.add_route("404", "/404")
    config.add_route("500", "/500")
    config.add_route("atramhasismenu", "/atramhasismenu")

    includeme(config)

    config.scan("pyoes.views")
    return config.make_wsgi_app()
