from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

import pytest
from jinja2 import Environment, FileSystemLoader, meta
from pyramid.interfaces import IRoutesMapper
from pyramid.paster import get_appsettings
from pyramid.request import Request

from pyoes import main


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def app():
    return main({}, **get_appsettings(str(ROOT / "development.ini")))


def test_only_required_templates_remain():
    templates = ROOT / "pyoes" / "templates"
    environment = Environment(
        loader=FileSystemLoader([templates, templates / "pyoes"]),
    )
    required = set()

    def visit(name):
        source, filename, _ = environment.loader.get_source(environment, name)
        path = Path(filename).relative_to(templates).as_posix()
        if path in required:
            return
        required.add(path)
        for dependency in meta.find_referenced_templates(environment.parse(source)):
            assert dependency is not None, f"Dynamic template dependency in {name}"
            visit(dependency)

    for name in (
        "index.jinja2",
        "typo.jinja2",
        "article.jinja2",
        "401.jinja2",
        "403.jinja2",
        "404.jinja2",
        "500.jinja2",
    ):
        visit(name)

    assert required == {
        path.relative_to(templates).as_posix() for path in templates.rglob("*.jinja2")
    }
    assert len(required) == 18


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.links.extend(value for key, value in attrs if key == "href")


@pytest.mark.parametrize(
    "path, content",
    [
        ("/", "Artikelpagina met 8/4-indeling"),
        ("/typo", "Typografie en iconen"),
        ("/article", "Erkende intergemeentelijke onroerenderfgoeddiensten"),
        ("/401", "De pagina is afgeschermd."),
        ("/403", "De pagina is afgeschermd."),
        ("/404", "De pagina werd niet gevonden."),
        ("/500", "Er is een technisch probleem."),
    ],
)
def test_demo_pages_render_with_valid_navigation(app, path, content):
    response = Request.blank(path).get_response(app)
    assert response.status_int == 200
    assert content in response.text

    parser = LinkParser()
    parser.feed(response.text)
    for href in parser.links:
        url = urlsplit(href)
        if not url.scheme and not url.netloc and url.path:
            assert url.path in {
                "/",
                "/typo",
                "/article",
                "/401",
                "/403",
                "/404",
                "/500",
            }


def test_home_links_to_all_demo_pages(app):
    response = Request.blank("/").get_response(app)
    parser = LinkParser()
    parser.feed(response.text)

    assert {"/typo", "/article", "/401", "/403", "/404", "/500"} <= set(parser.links)
    assert 'aria-labelledby="examples-title"' in response.text
    assert 'aria-labelledby="errors-title"' in response.text


@pytest.mark.parametrize(
    "path, active_href",
    [
        ("/", "/"),
        ("/typo", "/typo"),
        ("/article", "/article"),
        ("/401", None),
        ("/403", None),
        ("/404", None),
        ("/500", None),
    ],
)
def test_header_highlights_current_page(app, path, active_href):
    response = Request.blank(path).get_response(app)

    class NavigationParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.active_links = []
            self.bold_links = []

        def handle_starttag(self, tag, attrs):
            if tag != "a":
                return
            attributes = dict(attrs)
            if attributes.get("aria-current") == "page":
                self.active_links.append(attributes["href"])
            if "vl-link--bold" in attributes.get("class", "").split():
                self.bold_links.append(attributes["href"])

    parser = NavigationParser()
    parser.feed(response.text)
    expected = [active_href] if active_href is not None else []
    assert parser.active_links == expected
    assert parser.bold_links == expected


def test_only_retained_demo_routes_are_registered(app):
    routes = app.registry.queryUtility(IRoutesMapper).get_routes()
    assert {route.name for route in routes if not route.name.startswith("__")} == {
        "home",
        "typo",
        "article",
        "401",
        "403",
        "404",
        "500",
    }


@pytest.mark.parametrize("path", ["/colors", "/grids"])
def test_removed_demo_pages_return_not_found(app, path):
    assert Request.blank(path).get_response(app).status_int == 404
