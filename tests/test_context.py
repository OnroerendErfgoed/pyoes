import pytest
from jinja2 import Environment, PackageLoader, StrictUndefined
from pyramid import testing
from pyramid.events import BeforeRender
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.templating import Jinja2Templates
from starlette.testclient import TestClient

import pyoes.fastapi
from pyoes import includeme
from pyoes.context import PyoesContext
from pyoes.pyramid import PyramidContext


def environment():
    return Environment(
        loader=PackageLoader("pyoes", "templates"),
        undefined=StrictUndefined,
        autoescape=True,
    )


def make_context(**kw):
    return PyoesContext(
        route_path=lambda name, **params: f"/r/{name}/",
        static_path=lambda spec: f"/s/{spec}",
        **kw,
    )


class TestLayout:
    def render(self, ctx, **kw):
        return environment().get_template("pyoes/layout.jinja2").render(pyoes=ctx, **kw)

    def test_without_settings(self):
        html = self.render(make_context())
        assert 'href="/s/pyoes:static/css/app.css"' in html
        assert '<div class="vl-layout vl-u-spacer-top vl-u-spacer-bottom">' in html
        assert "plausible" not in html
        assert "widgets.vlaanderen.be/widget/live" in html

    def test_with_settings(self):
        html = self.render(
            make_context(
                plausible_domain_hash="hash",
                burgerprofiel_header_id="header-id",
                burgerprofiel_footer_id="footer-id",
                banner="Onderhoud",
                banner_detail="Meer uitleg",
                authenticated_userid="user",
            )
        )
        assert "hash.js" in html
        assert "/widget/header-id/embed" in html
        assert "/widget/footer-id/embed" in html
        assert "Onderhoud" in html and "Meer uitleg" in html
        assert 'loginUrl: "/r/home/aanmelden"' in html
        assert "websiteHasAuthenticatedSession = true" in html

    def test_template_variables_override_context(self):
        html = self.render(
            make_context(burgerprofiel_header_id="from-context"),
            burgerprofiel_header_id="from-template",
            home_route="/home/",
            css_files=["/custom.css"],
        )
        assert "/widget/from-template/embed" in html
        assert 'loginUrl: "/home/aanmelden"' in html
        assert 'href="/custom.css"' in html
        assert "app.css" not in html


def test_generate_uri():
    template = environment().from_string(
        "{% from 'pyoes/macros.jinja2' import generate_uri %}"
        "{{ generate_uri('https://id.erfgoed.net/{0}', 5) }}"
    )
    assert template.render().strip() == "https://id.erfgoed.net/5"


class TestPyramid:
    @pytest.fixture
    def config(self):
        config = testing.setUp(
            settings={
                "plausible.domain_hash": "hash",
                "burgerprofiel.header_id": "header-id",
                "pyoes.banner": "Onderhoud",
            }
        )
        config.add_route("home", "/")
        yield config
        testing.tearDown()

    def test_includeme_adds_context(self, config):
        includeme(config)
        config.commit()
        request = testing.DummyRequest()
        event = BeforeRender({"request": request})
        config.registry.notify(event)
        assert isinstance(event["pyoes"], PyramidContext)

    def test_context(self, config):
        ctx = PyramidContext(testing.DummyRequest())
        assert ctx.plausible_domain_hash == "hash"
        assert ctx.burgerprofiel_header_id == "header-id"
        assert ctx.burgerprofiel_footer_id is None
        assert ctx.banner == "Onderhoud"
        assert ctx.banner_detail is None
        assert ctx.home_url == "/"
        assert ctx.authenticated_userid is None
        assert ctx.user is None

    def test_render_layout(self, config):
        includeme(config)
        config.commit()
        ctx = PyramidContext(testing.DummyRequest())
        html = environment().get_template("pyoes/layout.jinja2").render(pyoes=ctx)
        assert "/widget/header-id/embed" in html
        assert "pyoes_static/css/app.css" in html


class TestFastAPI:
    @pytest.fixture
    def client(self):
        templates = Jinja2Templates(env=environment())

        def ctx(request):
            c = pyoes.fastapi.context(
                request,
                settings={
                    "burgerprofiel_header_id": "header-id",
                    "pyoes_banner": "Onderhoud",
                },
                user="user",
            )
            return JSONResponse(
                {
                    "header": c.burgerprofiel_header_id,
                    "banner": c.banner,
                    "user": c.user,
                    "home": c.home_url,
                    "query": c.route_path("home", _query={"a": [1, 2]}),
                    "pyoes_static": c.static_path("pyoes:static/css/app.css"),
                    "static": c.static_path("myapp:static/css/app.css"),
                }
            )

        def page(request):
            return templates.TemplateResponse(
                request,
                "pyoes/layout.jinja2",
                {"pyoes": pyoes.fastapi.context(request), "app_package": "pyoes"},
            )

        app = Starlette(
            routes=[
                Route("/", page, name="home"),
                Route("/ctx", ctx),
            ]
        )
        pyoes.fastapi.mount_static(app)
        pyoes.fastapi.mount_static(app, "/static", "static")
        return TestClient(app)

    def test_context(self, client):
        assert client.get("/ctx").json() == {
            "header": "header-id",
            "banner": "Onderhoud",
            "user": "user",
            "home": "/",
            "query": "/?a=1&a=2",
            "pyoes_static": "/pyoes_static/css/app.css",
            "static": "/static/css/app.css",
        }

    def test_render_layout(self, client):
        res = client.get("/")
        assert res.status_code == 200
        assert 'href="/pyoes_static/css/app.css"' in res.text

    def test_static_files(self, client):
        assert client.get("/pyoes_static/robots.txt").status_code == 200

    def test_settings_object(self):
        class Settings:
            plausible_domain_hash = "hash"

        c = pyoes.fastapi.context(None, settings=Settings(), banner="override")
        assert c.plausible_domain_hash == "hash"
        assert c.banner == "override"
        assert c.burgerprofiel_header_id is None
