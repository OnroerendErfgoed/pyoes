=======
Gebruik
=======

Opbouw
======

:mod:`pyoes` bestaat uit twee delen die samen gebruikt worden:

* het npm-package ``@OnroerendErfgoed/pyoes`` (map :file:`npm-packages/pyoes`)
  met de scss en de fonts;
* het python-package ``pyoes`` met de jinja2-templates van de gedeelde shell
  (header, navigatie, burgerprofiel, footer) en enkele macro's.

Sinds 0.27.0 is het `Webuniversum <https://overheid.vlaanderen.be/webuniversum>`_
(``@govflanders/vl-ui-design-system-style``) de basis van pyoes. Foundation en
font-awesome worden niet meer geladen, waardoor Webuniversum-componenten (ook in
Vue-onderdelen op dezelfde pagina) zonder conflicten werken.

CSS
===

Importeer in de :file:`app.scss` van je toepassing de entry ``pyoes-wu`` en
daarna je eigen stijlen:

.. code-block:: scss

    // optioneel: variabelen overschrijven VOOR de import, bv.
    // $primary-color: #944EA1;
    @import "@OnroerendErfgoed/pyoes/scss/pyoes-wu";
    @import "<package_name>";

Maak je eigen scss aan in :file:`/<package_name>/static/scss/_<package_name>.scss`.
De underscore zorgt ervoor dat dit bestand als partial gezien wordt en niet
afzonderlijk gecompileerd wordt.

Compileren gebeurt met `sass <https://sass-lang.com/dart-sass/>`_ (zie het
``compile-css`` script in de :file:`package.json` van de scaffold):

.. code-block:: bash

    $ cd <package_name>/static
    $ pnpm install
    $ pnpm run compile-css

Vergeet niet om :file:`app.css` in te checken (of ze in je build te genereren).

``pyoes-wu`` bevat:

* ``wu-settings``: de OE-variabelen (:file:`base-variables.scss`), het volledige
  Webuniversum en de OE-overrides (paars thema);
* ``pyoes-wu/oe-page``, ``oe-header`` en ``oe-banner``: de styling van de shell.

Enkele aandachtspunten bij de overstap van foundation naar Webuniversum:

* De root font-size is 62.5% (``1rem = 10px``), zoals in alle
  Webuniversum- en Vue-toepassingen. Rem-waarden in oude scss moeten herbekeken
  worden.
* De fonts worden door Webuniversum gedeclareerd ("Flanders Art Sans" met
  ``font-weight`` 300, 400, 500 en 700, plus italic). Gebruik dus
  ``font-weight: 500`` in plaats van de aparte families
  "Flanders Art Sans Medium" en dergelijke, en declareer zelf geen extra
  ``@font-face`` voor "Flanders Art Sans". De locatie van de fonts staat in
  ``$vl-font-location`` en ``$vl-icon-font-location`` en is standaard relatief
  aan :file:`static/css/app.css` (``../node_modules/@govflanders/...``).
* Het foundation-grid (``row``, ``columns``, ``panel``) bestaat niet meer;
  gebruik het Webuniversum-grid (``vl-grid``, ``vl-col--6-12``, ...) en de
  Webuniversum-componenten.
* Er wordt bewust geen css ``@layer`` gebruikt: Vue-bundels
  (vue_component_library) leveren Webuniversum ongelaagd mee en zouden anders
  altijd winnen van de shell.

De oude entries ``pyoes-settings``, ``pyoes-jinja`` en ``pyoes-apps`` (foundation)
blijven voorlopig beschikbaar voor toepassingen die nog niet gemigreerd zijn,
maar worden niet verder ontwikkeld.

Jinja2 templates
================

:mod:`pyoes` levert een globale layout :file:`pyoes/layout.jinja2` die de
header, de navigatie en de burgerprofiel-header en -footer levert. De pagina
volgt de Webuniversum-structuur:

.. code-block:: text

    .vl-page
      [burgerprofiel-header]              block vlaanderen_header
      header.vl-application-header        block header (pyoes/header.jinja2)
      main.vl-main-content                block main
        .vl-region > .vl-layout
          block messages
          block content
      #footerContainer                    block vlaanderen_footer, block footer
    block javascript

Maak in je toepassing een eigen :file:`layout.jinja2` aan waarin je de zaken
instelt die voor de ganse site van tel zijn:

.. code-block:: jinja

    {% extends "pyoes/layout.jinja2" %}

    {% set app_package = '<package_name>' %}
    {% set active_title = 'Mijn toepassing' %}

    {% set main_nav = [
        ('home', 'Home', request.route_path('home')),
        ('zoeken', 'Zoeken', request.route_path('zoeken')),
    ] -%}

    {% set dropdown_main_nav = [
        ('beheer', 'Beheer', [
            ('gebruikers', 'Gebruikers', request.route_path('gebruikers')),
            ('instellingen', 'Instellingen', request.route_path('instellingen')),
        ])
    ] -%}

    {% set nav_actions = [
        ('Contact', request.route_path('contact')),
    ] -%}

    {% set header_links = [
        ('Over ons', 'https://www.onroerenderfgoed.be/over-ons', 'Meer informatie over ons'),
    ] -%}

De beschikbare variabelen:

``app_package``
    Het package dat :file:`static/css/app.css` levert (standaard ``pyoes``).
``css_files``, ``js_files``
    Lijsten met te laden stylesheets en scripts. Standaard wordt enkel
    :file:`app.css` geladen en geen javascript: de shell heeft er geen nodig.
``active_title``, ``home_link``
    De titel in de header en de link erachter.
``header_links``
    Lijst van ``(tekst, href, title)``; extra links rechtsboven in de header.
``main_nav``
    Lijst van ``(id, caption, href)`` of ``(id, caption, href, class)``; het
    item met id ``home`` wordt als huisje getoond.
``dropdown_main_nav``
    Lijst van ``(id, caption, submenu)`` met submenu een lijst van
    ``(id, caption, href)``; wordt een uitklapmenu zonder javascript.
``active_main_nav``
    Het id van het actieve navigatie-item (krijgt ``aria-current="page"``).
``nav_actions``
    Lijst van ``(caption, href)``; acties rechts in de navigatiebalk.
``plausible_domain_hash``, ``plausible_omgeving``, ``burgerprofiel_header_id``,
``burgerprofiel_footer_id``
    Standaard uit de ini-settings; zie :file:`development.ini`.

``login_nav``, ``login_sub_nav``
    Accountmenu rechts in de navigatiebalk (standaard leeg). Zonder aangemelde
    gebruiker worden de ``(caption, href)`` van ``login_nav`` getoond, met een
    aangemelde gebruiker (``request.user``) een uitklapmenu met de naam van de
    gebruiker en de ``login_sub_nav``-links.

In je individuele templates erf je van je eigen layout en vul je ``content``
in met Webuniversum-markup:

.. code-block:: jinja

    {% extends "layout.jinja2" %}

    {% set active_main_nav = 'zoeken' %}

    {% block content %}
    <div class="vl-grid">
        <div class="vl-col--3-12 vl-col--12-12--s">
            <nav>
                <h2 class="vl-title vl-title--h3">Een submenu</h2>
                ...
            </nav>
        </div>
        <div class="vl-col--9-12 vl-col--12-12--s vl-typography">
            <h1 class="vl-title vl-title--h1">Over deze site</h1>
            <p>Lorem ipsum dolor sit amet, ...</p>
        </div>
    </div>
    {% endblock %}

Wil je de inhoud niet in een ``vl-region`` / ``vl-layout``, overschrijf dan het
block ``main`` in plaats van ``content``.

Onderhoudsbanner
----------------

Met de settings ``pyoes.banner`` en ``pyoes.banner.detail`` verschijnt een
boodschap in de burgerprofiel-header, met een popup voor de details.

Demonstratie
============

Als je gewoon eens de stijl wenst te bekijken, draai dan de demo-toepassing.
Ze zit in de pyoes repository, maar wordt niet verdeeld in de pyoes package.

.. code-block:: bash

    $ git clone https://github.com/OnroerendErfgoed/pyoes pyoes_demo
    $ cd pyoes_demo
    $ mise install
    $ mise run server

Zie de :file:`README.md` voor de details van de lokale ontwikkelomgeving.

De templates van de demo vind je in :file:`pyoes/templates`, de algemene pyoes
templates die door andere toepassingen worden overgenomen in
:file:`pyoes/templates/pyoes`. De :file:`pyoes/static` folder bevat de scss van
de demo-toepassing.
