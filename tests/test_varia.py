# -*- coding: utf8 -*-

from __future__ import unicode_literals

import pytest
from jinja2 import Environment, PackageLoader, StrictUndefined
from pyramid import testing

from pyoes import includeme


class TestIncludeMe:

    def test_includeme(self):
        config = testing.setUp()
        includeme(config)
        del config


@pytest.fixture
def environment():
    return Environment(
        loader=PackageLoader("pyoes", "templates"),
        undefined=StrictUndefined,
        autoescape=True,
    )


class DummyRequest:
    """Minimale request voor het renderen van pyoes/layout.jinja2."""

    def __init__(self, settings=None, authenticated_userid=None):
        self.registry = testing.DummyResource()
        self.registry.settings = {
            "plausible.domain_hash": None,
            "burgerprofiel.header_id": None,
            "burgerprofiel.footer_id": None,
            "pyoes.banner": None,
            "pyoes.banner.detail": None,
        }
        self.registry.settings.update(settings or {})
        self.authenticated_userid = authenticated_userid

    def route_path(self, name, *args, **kwargs):
        return "/" if name == "home" else "/" + name

    def static_path(self, path):
        package, _, rest = path.partition(":")
        return "/{}_{}".format(package, rest)


class TestHeaderNavActions:

    @pytest.mark.parametrize(
        "context",
        [
            {},
            {"nav_actions": []},
            {"login_nav": [], "login_sub_nav": []},
        ],
    )
    def test_no_actions(self, environment, context):
        html = environment.get_template("pyoes/header.jinja2").render(**context)
        assert "oe-navigation__actions" not in html
        assert "Aanmelden" not in html
        assert "Afmelden" not in html

    def test_login_nav_anonymous(self, environment):
        html = environment.get_template("pyoes/header.jinja2").render(
            login_nav=[("Aanmelden", "/login")],
            login_sub_nav=[("Afmelden", "/logout")],
            request={"user": None, "authenticated_userid": None},
        )
        assert "oe-navigation__actions" in html
        assert 'href="/login" rel="nofollow">Aanmelden</a>' in html
        assert "Afmelden" not in html

    def test_login_nav_authenticated(self, environment):
        html = environment.get_template("pyoes/header.jinja2").render(
            login_nav=[("Aanmelden", "/login")],
            login_sub_nav=[("Profiel", "/profiel"), ("Afmelden", "/logout")],
            request={
                "user": {"actor": {"omschrijving": "Account name"}},
                "authenticated_userid": "username",
            },
        )
        assert "Account name" in html
        assert "<details>" in html
        assert 'href="/logout">Afmelden</a>' in html
        assert "Aanmelden" not in html

    @pytest.mark.parametrize(
        "context",
        [
            {},
            {
                "request": {
                    "user": None,
                    "authenticated_userid": None,
                }
            },
            {
                "request": {
                    "user": {"actor": {"omschrijving": "Account name"}},
                    "authenticated_userid": "username",
                }
            },
        ],
    )
    def test_actions_ignore_login_state(self, environment, context):
        html = environment.get_template("pyoes/header.jinja2").render(
            nav_actions=[("Contact", "/contact"), ("Help & support", "/help")],
            **context,
        )
        assert "oe-navigation__actions" in html
        assert 'href="/contact">Contact</a>' in html
        assert 'href="/help">Help &amp; support</a>' in html
        assert "Account name" not in html
        assert "username" not in html

    def test_actions_block_override(self, environment):
        template = environment.from_string(
            '{% extends "pyoes/header.jinja2" %}'
            "{% block nav_actions %}<button>Help</button>{% endblock %}"
        )
        assert "<button>Help</button>" in template.render()


class TestHeader:

    def test_webuniversum_markup(self, environment):
        html = environment.get_template("pyoes/header.jinja2").render(
            active_title="Mijn toepassing",
            home_link="/start",
            header_links=[("Over ons", "https://example.org", "Meer info")],
        )
        assert 'class="vl-application-header oe-header vl-application-header--has-actions"' in html
        assert 'href="/start">Mijn toepassing</a>' in html
        assert 'class="oe-header__logo"' in html
        assert 'class="vl-application-header__action"' in html
        assert 'href="https://example.org" target="_blank" rel="noopener"' in html
        # geen foundation meer
        assert "top-bar" not in html
        assert "columns" not in html
        assert "fa fa-" not in html

    def test_main_nav_active_item(self, environment):
        html = environment.get_template("pyoes/header.jinja2").render(
            main_nav=[
                ("home", "Home", "/"),
                ("zoeken", "Zoeken", "/zoeken"),
                ("beheer", "Beheer", "/beheer", "extra-class"),
            ],
            active_main_nav="zoeken",
        )
        assert 'class="vl-link vl-link--bold" href="/zoeken" aria-current="page"' in html
        assert 'class="vl-link" href="/beheer"' in html
        assert "vl-application-header__sub__action extra-class" in html
        assert "vl-vi-places-home" in html
        assert '<span class="vl-u-visually-hidden">Home</span>' in html

    def test_dropdown_nav(self, environment):
        html = environment.get_template("pyoes/header.jinja2").render(
            dropdown_main_nav=[
                ("fouten", "Fouten", [("404", "Niet gevonden", "/404")])
            ],
            active_main_nav="404",
        )
        assert "<details>" in html
        assert 'aria-current="true"' in html
        assert 'href="/404" aria-current="page">Niet gevonden</a>' in html


class TestLayout:

    def test_layout_structure(self, environment):
        html = environment.get_template("pyoes/layout.jinja2").render(
            request=DummyRequest()
        )
        assert '<div class="vl-page">' in html
        assert '<main class="vl-main-content" id="main">' in html
        assert '<section class="vl-region">' in html
        assert '<div class="vl-layout">' in html
        assert 'href="/pyoes_static/css/app.css"' in html
        # standaard geen eigen javascript (geen foundation/jquery) meer; enkel
        # de vlaanderen-widgets blijven over
        assert '<script src="/pyoes_static' not in html
        assert "foundation" not in html
        assert "jquery" not in html
        assert 'class="container"' not in html
        assert "columns" not in html

    def test_layout_js_and_css_files(self, environment):
        html = environment.get_template("pyoes/layout.jinja2").render(
            request=DummyRequest(),
            css_files=["/a.css"],
            js_files=["/a.js"],
        )
        assert '<link rel="stylesheet" href="/a.css"/>' in html
        assert "app.css" not in html
        assert '<script src="/a.js"></script>' in html

    def test_layout_burgerprofiel_and_banner(self, environment):
        html = environment.get_template("pyoes/layout.jinja2").render(
            request=DummyRequest(
                settings={
                    "burgerprofiel.header_id": "header-id",
                    "burgerprofiel.footer_id": "footer-id",
                    "pyoes.banner": "Onderhoud",
                    "pyoes.banner.detail": "Details",
                },
                authenticated_userid="user",
            ),
            plausible_omgeving="prod",
        )
        assert "widget/header-id/embed" in html
        assert "widget/footer-id/embed" in html
        assert "widgets.vlaanderen.be/widget/live" not in html
        assert 'id="onderhoud-popup"' in html
        assert "Onderhoud" in html
        assert "Details" in html
        assert "class=\"row" not in html

    def test_layout_blocks_overridable(self, environment):
        template = environment.from_string(
            '{% extends "pyoes/layout.jinja2" %}'
            "{% block main %}<div id=\"custom-main\"></div>{% endblock %}"
            "{% block footer %}<p>footer</p>{% endblock %}"
        )
        html = template.render(request=DummyRequest())
        assert '<div id="custom-main"></div>' in html
        assert "vl-region" not in html
        assert "<p>footer</p>" in html

    def test_footer_include(self, environment):
        html = environment.get_template("pyoes/footer.jinja2").render(
            footer_nav=[("Toegankelijkheid", "https://example.org/toegankelijkheid")]
        )
        assert 'class="oe-footer vl-region"' in html
        assert 'href="https://example.org/toegankelijkheid">Toegankelijkheid</a>' in html
        assert "columns" not in html
