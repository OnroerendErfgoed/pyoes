pyoes: Pyramid OE style
=======================

Pyoes is een package om het makkelijker te maken om layout te delen tussen de verschillende OE sites.

Informatie over het werken met deze bibliotheek kun je vinden in de :file:`docs` 
folder. Deze kan gebuild worden tot propere documentatie met behulp van 
`Sphinx <http://sphinx-doc.org>`_.

Zorg dat Sphinx wel aanwezig is in de virtual environment waarin je pyramid_oeauth
hebt geïnstalleerd.

.. code-block:: bash

    # activeer de virtual env
    $ pip install sphinx
    $ cd docs
    $ make html
    # Indien je een latex toolchain hebt op je systeem kun je ook een pdf bouwen.
    $ make latexpdf
