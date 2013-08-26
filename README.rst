pyoes: Pyramid OE style
=======================

Pyoes is een package om het makkelijker te maken om layout te delen tussen de verschillende OE sites.

Installeren
-----------

- Een link toevoegen naar github in setup.py (net zoals bv. pyramid_oeauth)
- De compass extension lokaal kopieren: install_compass_extensions
- Voeg de pyoes:templates dir toe aan je jinja2.directories
- Zorg dat je compass hebt geïnstalleerd op je systeem (is een ruby package)
- Installeer de compass extension in je static dir

.. code-block:: bash

    $ cd static
    $ compass install pyoes

- Als je aan css werkt is het best om compass je files te laten monitoren zodat 
  deze wanneer nodig kan hercompileren.

.. code-block:: bash
    
    $ cd static
    $ compass watch .
    # je kunt ook gewoon eenmalig compileren
    $ compass compile

- Er zijn een aantal statische files nodig die meegeleverd worden met pyoes. Om 
  deze te kunnen gebruiken moeten je een static view registeren.

.. code-block:: python

    config.add_static_view('pyoes_static', 'pyoes:static')

Een overzicht van de stijl krijgen
----------------------------------

- Maak een git clone van deze repository
- Maak een virtualenv

.. code-block:: bash
    
    $ mkvirtualenv pyoes

- Installeer de dependencies

.. code-block:: bash

    $ python setup.py install

- Start pyramid

.. code-block:: bash
    
    $ pserve development.ini
