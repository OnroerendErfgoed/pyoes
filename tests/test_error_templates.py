import re

import pytest
from jinja2 import ChoiceLoader, DictLoader, Environment, PackageLoader, StrictUndefined


@pytest.fixture
def environment():
    return Environment(
        loader=ChoiceLoader(
            [
                DictLoader(
                    {
                        "layout.jinja2": (
                            "<title>{% block html_title %}{% endblock %}</title>"
                            "{% block content %}{% endblock %}"
                        ),
                    }
                ),
                PackageLoader("pyoes", "templates"),
            ]
        ),
        undefined=StrictUndefined,
        autoescape=True,
    )


@pytest.mark.parametrize(
    "status, message, advice_count",
    [
        (401, "De pagina is afgeschermd.", 1),
        (403, "De pagina is afgeschermd.", 1),
        (404, "De pagina werd niet gevonden.", 3),
        (500, "Er is een technisch probleem.", 4),
    ],
)
def test_error_page_uses_wu_classes(environment, status, message, advice_count):
    html = environment.get_template(f"{status}.jinja2").render()

    assert '<main class="vl-grid vl-u-spacer-top vl-u-spacer-bottom">' in html
    assert 'class="vl-col--1-1"' in html
    assert 'class="vl-title vl-title--h1"' in html
    assert 'class="vl-vi vl-vi-warning" aria-hidden="true"' in html
    assert 'class="vl-info-tile vl-typography"' in html
    assert f"<span>{status}</span>" in html
    assert message in html
    assert "Wat kan je zelf doen?" in html
    assert html.count("<li>") == advice_count
    assert 'class="vl-link" href="mailto:ict@onroerenderfgoed.be"' in html
    assert ('class="vl-link" href="/"' in html) == (status in (404, 500))
    assert "style=" not in html
    assert "</br>" not in html
    for classes in re.findall(r'class="([^"]+)"', html):
        assert all(name.startswith("vl-") for name in classes.split())


@pytest.mark.parametrize(
    "status, mailto_variable",
    [
        (401, "mailto_error"),
        (403, "mailto_error"),
        (404, "mailto_notfound"),
        (500, "mailto_error"),
    ],
)
def test_error_page_context_overrides(environment, status, mailto_variable):
    html = environment.get_template(f"{status}.jinja2").render(
        **{mailto_variable: "help@example.be", "app_package": "Test & app"},
    )

    assert 'class="vl-link" href="mailto:help@example.be">help@example.be</a>' in html
    assert "ict@onroerenderfgoed.be" not in html
    assert "Test &amp; app" in html
