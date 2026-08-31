pyoes: Pyramid OE style
=======================

.. image:: https://travis-ci.org/OnroerendErfgoed/pyoes.png
        :target: https://travis-ci.org/OnroerendErfgoed/pyoes
.. image:: https://coveralls.io/repos/OnroerendErfgoed/pyoes/badge.png?branch=master
        :target: https://coveralls.io/r/OnroerendErfgoed/pyoes

.. image:: https://readthedocs.org/projects/pyoes/badge/?version=latest
        :target: https://readthedocs.org/projects/pyoes/?badge=latest
        :alt: Documentation Status
.. image:: https://badge.fury.io/py/pyoes.png
        :target: http://badge.fury.io/py/pyoes

Pyoes helps to share layout between different websites and applications of
Onroerend Erfgoed (Flanders Heritage).

Lokale ontwikkelomgeving (mise)
-------------------------------

Deze repo gebruikt `mise <https://mise.jdx.dev/>`_ om de project setup zo simpel
mogelijk te maken.

Vereisten
~~~~~~~~~

- `mise <https://mise.jdx.dev/getting-started/>`_

Meer is er niet nodig: pyoes heeft **geen service containers** (geen databank,
elasticsearch, redis of minio) en dus ook geen ``docker-compose.yml`` of
``mise run docker``. Er zijn ook **geen secrets**: ``development.ini`` staat
gewoon in de repo, dus er is geen gpg-key, geen ``wildcards-private.yaml`` en
geen ``transform``-stap (en dus ook geen ``encrypt``-task).

Vanaf een verse clone
~~~~~~~~~~~~~~~~~~~~~

Drie commando's:

.. code-block:: bash

    $ mise trust       # vertrouw deze config (afhankelijk van je settings)
    $ mise install     # installeert alle tools (python, uv, node, yarn, pre-commit)
    $ mise run server  # setup (1e keer) + start de demo server

``mise run server`` draait de eerste keer automatisch ``mise run setup`` (als er
nog geen virtualenv of gecompileerde css is) en start daarna de server op
http://local.onroerenderfgoed.be:6543 (die hostname moet in je ``/etc/hosts``
naar ``127.0.0.1`` wijzen).

``mise run setup`` zet de volledige backend + frontend op: de virtualenv met de
dependencies uit ``requirements-dev.txt``, pyoes zelf editable geïnstalleerd, de
pre-commit hooks, en de frontend in ``pyoes/static`` (``yarn install`` +
``yarn compile-css``, wat ``pyoes/static/css/app.css`` genereert - die is
git-ignored). ``npm-packages/pyoes`` wordt als ``file:``-dependency mee
geïnstalleerd; een aparte ``yarn install`` is daar niet nodig.

Vanaf een bestaande clone
~~~~~~~~~~~~~~~~~~~~~~~~~

Is alles al opgezet, dan heb je enkel nog dit nodig:

.. code-block:: bash

    $ mise run server  # start meteen de demo server

Je eventueel aangepaste ``development.ini`` blijft daarbij behouden: setup
genereert die file niet, ze is gewoon gecommit.

mise activeren in je shell
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ echo 'eval "$(mise activate bash)"' >> ~/.bashrc   # ~/.zshrc voor zsh

Zo wordt de virtualenv automatisch geactiveerd zodra je in deze repo zit (geen
``source .venv/bin/activate`` meer nodig). Dezelfde virtualenv is ook actief
binnen ``mise run`` en ``mise exec``.

Overige commando's
~~~~~~~~~~~~~~~~~~

- ``mise run setup`` - expliciet de volledige backend + frontend setup draaien
- ``mise run test`` - draait de testsuite (pytest)
- ``mise run check-versions`` - controleert of de versies in ``pyproject.toml``,
  ``npm-packages/pyoes/package.json`` en ``pyoes/static/package.json`` gelijk
  zijn (dezelfde check als in CI)
- ``mise run pip-compile`` - hergenereert de ``requirements*.txt`` uit
  ``pyproject.toml``
- ``mise run build`` - bouwt de wheel + sdist (``build:wheel`` / ``build:sdist``
  voor één van beide)
- ``mise run cleanup`` - verwijdert alles wat ``setup`` aanmaakt (``.venv``,
  ``node_modules``, ``pyoes/static/css``, ``dist``)

``mise tasks`` geeft altijd de volledige, actuele lijst.

Requirements updaten
~~~~~~~~~~~~~~~~~~~~

De dependencies staan in ``pyproject.toml``. Pas ze daar aan en draai daarna
``mise run pip-compile`` om ``requirements.txt`` (runtime),
``requirements-ci.txt`` en ``requirements-dev.txt`` (beide de ``dev`` extra)
opnieuw te genereren met uv. pyoes gebruikt enkel publieke PyPI packages, dus
hiervoor is geen VPN of interne index nodig.

uv behoudt bestaande pins en verhoogt enkel wat nodig is. Wil je echt alles naar
de hoogste versies updaten, voeg dan ``--upgrade`` toe aan het uv-commando in
``scripts/pip_compile.sh``.

More information about this library can be found in the docs `folder`. These can
be build using `Sphinx <http://sphinx-doc.org>`_.

.. code-block:: bash

    # activate your virtual env
    $ pip install -r requirements-dev.txt
    $ cd docs
    $ make html
    # You can also build a pdf, provided you have the correct latex toolchain installed.
    $ make latexpdf
