===========
Installatie
===========

Om :mod:`pyoes` te installeren, zijn er twee mogelijkheden. Ofwel installeer
je rechtstreeks vanaf :term:`Github`, ofwel doe je eerst een lokale checkout
en installeer je vanaf deze checkout.

Om rechtstreeks te installeren van Github moet je de :file:`setup.py` van
je toepassing aanpassen. Enerzijds moet je :mod:`pyoes` toevoegen 
als requirement en anderzijds moet je een dependecy links toevoegen. Dit is
een link die aan de setup laat weten waar een bepaalde package kan gevonden 
worden. In deze url moet je ook de aanmeldgegevens meegeven. Gebruik hiervoor
de gebruiker *IndustrieelErfgoed*, deze heeft enkel leesrechten op de code.

.. code-block:: python

    requires = [                                                                    
        'pyramid',
        'pyoes>=0.1.0'
    ]

    setup(
        ...,
        dependency_links = [                                                      
            'https://IndustrieelErfgoed:<<PWD>>@github.com/OnroerendErfgoed/pyoes/tarball/0.1.0#egg=pyoes-0.1.0'
        ]
     )   


Ofwel maak je een lokale checkout van :mod:`pyoes`, dit kun je doen 
met je eigen account als deze rechten heeft op de git repository. Daarna kun 
je de code builden tot een sdist met via het :file:`setup.py` script van 
:mod:`pyoes`. De resulterende sdist kun je dan installeren via pip.

.. code-block:: bash

    $ git clone https://github.com/OnroerendErfgoed/pyoes
    $ cd pyoes
    $ python setup.py sdist
    $ // activeer nu de virtual env van de pyramid app
    $ pip install dist/pyoes-0.1.0.tar.gz

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
