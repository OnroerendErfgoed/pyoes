"""
Pyramid integration: ``config.include("pyoes")`` serves the pyoes static files
and makes the ``pyoes`` template context available in every rendered template.
"""

from pyramid.config import Configurator
from pyramid.events import BeforeRender
from pyramid.path import AssetResolver

from pyoes.cachebust import PARAM
from pyoes.cachebust import file_hash


class ContentHashCacheBuster:
    """
    Pyramid cache buster adding ``?v=<hash of the file contents>`` to urls
    generated with ``request.static_path`` / ``request.static_url``. Files that
    can not be found on disk are left untouched.

    .. code-block:: python

        config.add_static_view("static", "myapp:static")
        config.add_cache_buster("myapp:static/", ContentHashCacheBuster())
    """

    def __init__(self, param=PARAM):
        self.param = param

    def __call__(self, request, subpath, kw):
        try:
            path = AssetResolver().resolve(kw["rawspec"]).abspath()
        except (KeyError, ValueError, ImportError):
            return subpath, kw
        token = file_hash(path)
        if token is not None:
            query = kw.setdefault("_query", {})
            if isinstance(query, dict):
                query[self.param] = token
            else:
                kw["_query"] = (*query, (self.param, token))
        return subpath, kw


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
    def burgerprofiel_version(self):
        return self._setting("burgerprofiel.version")

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
    config.add_cache_buster("pyoes:static/", ContentHashCacheBuster())
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
    config.add_route("typo", "/typo")
    config.add_route("article", "/article")
    config.add_route("burgerprofielv5", "/burgerprofielv5")
    config.add_route("burgerprofielv5_2", "/burgerprofielv5_2")
    config.add_route("401", "/401")
    config.add_route("403", "/403")
    config.add_route("404", "/404")
    config.add_route("500", "/500")

    includeme(config)

    config.scan("pyoes.views")
    return config.make_wsgi_app()
