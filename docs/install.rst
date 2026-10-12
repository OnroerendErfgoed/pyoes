===========
Installatie
===========

Python package
==============

Voeg ``pyoes`` toe aan de dependencies van je Pyramid-applicatie, bijvoorbeeld
in :file:`pyproject.toml` of :file:`requirements.txt`, en installeer deze met
de package manager van je project.

Je kunt het package ook rechtstreeks installeren:

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

Stylesheets
===========

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
