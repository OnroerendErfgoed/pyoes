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


class TestHeaderNavActions:

    @pytest.fixture
    def environment(self):
        return Environment(
            loader=PackageLoader("pyoes", "templates"),
            undefined=StrictUndefined,
            autoescape=True,
        )

    @pytest.mark.parametrize(
        "context",
        [
            {},
            {"nav_actions": []},
            {
                "login_nav": [("Aanmelden", "/login")],
                "login_sub_nav": [("Afmelden", "/logout")],
            },
        ],
    )
    def test_no_actions(self, environment, context):
        html = environment.get_template("pyoes/header.jinja2").render(**context)
        assert "oe-navigation__actions" not in html
        assert "Aanmelden" not in html
        assert "Afmelden" not in html

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

    def test_mobile_menu(self, environment):
        html = environment.get_template("pyoes/header.jinja2").render(
            header_links=[("External", "/external", "External site")],
            dropdown_main_nav=[("more", "More", [("help", "Help", "/help")])],
            nav_actions=[("Contact", "/contact")],
        )
        assert '<details class="oe-navigation__menu">' in html
        assert '<summary class="oe-navigation__toggle">' in html
        assert 'vl-vi-menu" aria-hidden="true"' in html
        assert "oe-navigation__header-link" in html
        assert html.count('href="/external"') == 2
        assert 'href="/help"' in html
        assert 'href="/contact"' in html
