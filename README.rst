pyoes: Pyramid OE style
=======================

.. image:: https://travis-ci.org/OnroerendErfgoed/pyoes.png
        :target: https://travis-ci.org/OnroerendErfgoed/pyoes
.. image:: https://coveralls.io/repos/OnroerendErfgoed/pyoes/badge.png?branch=master
        :target: https://coveralls.io/r/OnroerendErfgoed/pyoes
.. image:: https://badge.fury.io/py/pyoes.png
        :target: http://badge.fury.io/py/pyoes

Pyoes is een package om het makkelijker te maken om layout te delen tussen de verschillende OE
(Onroerend Erfgoed) sites.

Informatie over het werken met deze bibliotheek kun je vinden in de `docs` 
folder. Deze kan gebuild worden tot propere documentatie met behulp van 
`Sphinx <http://sphinx-doc.org>`_.

Zorg dat Sphinx wel aanwezig is in de virtual environment waarin je pyoes hebt geïnstalleerd.

.. code-block:: bash

    # activeer de virtual env
    $ pip install sphinx
    $ cd docs
    $ make html
    # Indien je een latex toolchain hebt op je systeem kun je ook een pdf bouwen.
    $ make latexpdf
