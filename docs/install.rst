===========
Installatie
===========

Installatie
===========

Om :mod:`pyoes` te installeren, werk je best met de package die op pypi te 
vinden is. Om te installeren vanaf pypi moet je eenvoudigweg een dependency op 
pyoes declareren in :file:`setup.py` en zorgen dat pypi bereikbaar is.

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

    $ git clone https://github.com/OnroerendErfgoed/pyoes
    $ cd pyoes
    $ python setup.py sdist
    $ // activeer nu de virtual env van de pyramid app
    $ pip install dist/pyoes-0.3.2.tar.gz

Je kan :mod:`pyoes` ook in de :file:`requirements.txt` toevoegen. Deze zal dan mee installeren
wanneer de requirements geïnstalleerd worden.

.. code-block:: ini

    pyoes==0.3.2

Als je op de master versie wil werken moet je deze lijn toevoegen:

.. code-block:: ini

    -e git+https://github.com/OnroerendErfgoed/pyoes.git@master#egg=pyoes

Scaffolds worden niet meer meegeleverd. Maak de applicatiespecifieke
:file:`static` en :file:`templates` directories zelf aan. Maak een eigen
:file:`layout.jinja2` die :file:`pyoes/layout.jinja2` uitbreidt, zoals beschreven
in :doc:`gebruik`.

:mod:`pyoes` komt met een set van :term:`Jinja2` templates. Om deze te kunnen gebruiken, 
moet je wel nog de parameter jinja2.directories correct instellen. Daarnaast 
zijn er ook nog filters die je kunt toevoegen aan je project.

.. code-block:: ini

    jinja2.directories =
        <package_name>:templates
        pyoes:templates
    jinja2.filters = 
        setattr = pyoes.utils.set_attr_filter

Tenslotten moet je :mod:`pyoes` toevoegen aan je main functie. Dit zorgt er voor
dat de correcte static dir wordt toegevoegd en dat een aantal static views 
geregistreerd worden.

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


Update
======

Werk bij een nieuwe versie van :mod:`pyoes` de dependency van je applicatie bij
en raadpleeg :doc:`changes` voor eventuele aanpassingen. Bestaande
applicatiespecifieke templates en statische bestanden blijven behouden en
moeten indien nodig handmatig bijgewerkt worden.

De :term:`Jinja2` templates zijn automatisch beschikbaar. Als er nieuwe filters zijn 
toegevoegd, moet je deze wel nog toevoegen aan je `.ini` bestand.
