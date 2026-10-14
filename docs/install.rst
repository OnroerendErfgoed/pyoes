===========
Installatie
===========

Python package
==============

Voeg ``pyoes`` toe aan de dependencies van je Pyramid-applicatie, bijvoorbeeld
in :file:`pyproject.toml` of :file:`requirements.txt`, en installeer deze met
de package manager van je project.

.. code-block:: python

    requires = [
        'pyramid',
        'pyoes[pyramid]'
    ]

Pyramid is een optionele dependency: gebruik ``pyoes[pyramid]`` voor een pyramid
applicatie en ``pyoes[fastapi]`` voor een FastAPI applicatie (zie :ref:`fastapi`).

Ofwel maak je een lokale checkout van :mod:`pyoes`, dit kun je doen 
met je eigen account als deze rechten heeft op de git repository. Daarna kun 
je de code builden tot een sdist met via het :file:`setup.py` script van 
:mod:`pyoes`. De resulterende sdist kun je dan installeren via pip.

.. code-block:: bash

    $ pip install pyoes

Jinja2 templates
================

:mod:`pyoes` levert gedeelde :term:`Jinja2` templates. Configureer de
template directories en de filters in het :file:`.ini` bestand van je
applicatie:

.. code-block:: ini

    jinja2.directories =
        <package_name>:templates
        pyoes:templates
    jinja2.filters =
        setattr = pyoes.utils.set_attr_filter

Maak zelf een :file:`templates/layout.jinja2` in je applicatie die erft van
``pyoes/layout.jinja2``. Zie :doc:`gebruik` voor een voorbeeld van de
applicatiespecifieke instellingen.

Voeg :mod:`pyoes` toe aan de configuratie van je applicatie om de static
directory en de static views te registreren:

.. code-block:: python

    config.include('pyoes')

Dit maakt ook de ``pyoes`` variabele beschikbaar in elke template. De pyoes
templates halen hun instellingen (``plausible.domain_hash``,
``burgerprofiel.header_id``, ``burgerprofiel.footer_id``, ``pyoes.banner`` en
``pyoes.banner.detail``) en urls daaruit, en niet meer rechtstreeks uit
``request``. Zonder ``config.include('pyoes')`` werken de templates dus niet.

.. _fastapi:

FastAPI
=======

In een FastAPI (of Starlette) applicatie zijn er geen ``.ini`` settings en geen
pyramid ``request``. Daar bouw je de ``pyoes`` template context zelf op met
:func:`pyoes.fastapi.context` en geef je die mee bij het renderen.

.. code-block:: python

    from fastapi.staticfiles import StaticFiles
    from fastapi.templating import Jinja2Templates
    from jinja2 import ChoiceLoader, Environment, FileSystemLoader, PackageLoader

    import pyoes.fastapi

    app.mount("/static", StaticFiles(directory="myapp/static"), name="static")
    pyoes.fastapi.mount_static(app)  # /pyoes_static

    templates = Jinja2Templates(env=Environment(
        loader=ChoiceLoader([
            FileSystemLoader("myapp/templates"),
            PackageLoader("pyoes", "templates"),
        ]),
        autoescape=True,  # jinja2 staat standaard autoescape uit
    ))

    def render(request, name, context=None, user=None):
        pyoes_context = pyoes.fastapi.context(
            request, settings=get_settings(), user=user,
            authenticated_userid=user.userid if user else None,
        )
        return templates.TemplateResponse(
            request, name, {"pyoes": pyoes_context, **(context or {})}
        )

``settings`` mag een object (bv. pydantic ``BaseSettings``) of een dict zijn met
de optionele attributen ``plausible_domain_hash``, ``burgerprofiel_header_id``,
``burgerprofiel_footer_id``, ``pyoes_banner`` en ``pyoes_banner_detail``.

Routes waarnaar de templates verwijzen moeten een naam hebben, minstens
``home`` (``@app.get("/", name="home")``), tenzij je ``home_route`` zelf
instelt in je layout. Asset specs zoals ``myapp:static/css/app.css`` worden
vertaald naar de ``static`` mount, ``pyoes:static/...`` naar ``pyoes_static``.

De gedeelde stylesheets worden afzonderlijk aangeboden als npm-package
``@OnroerendErfgoed/pyoes`` via GitHub Packages. Beheer de frontend
dependencies en de Sass-build in je eigen applicatie.

Voor de lokale demo bevat deze repository een volledige pnpm- en
Sass-configuratie. Voer vanuit de repository-root het volgende uit:

.. code-block:: bash

    $ mise run setup

Dit installeert de Python- en frontend-dependencies en compileert de CSS.
Zie :doc:`gebruik` voor het opnieuw compileren van de stylesheets.

Update
======

Werk de ``pyoes`` dependency bij met de package manager van je applicatie.
De gedeelde Jinja2 templates zijn daarna automatisch beschikbaar. Eigen
templates en static bestanden blijven onder beheer van je applicatie.
Voeg eventuele nieuwe filters zelf toe aan het :file:`.ini` bestand.

Werk indien nodig ook het npm styles-package bij en compileer de CSS
opnieuw. Raadpleeg :doc:`changes` voor wijzigingen tussen versies.
