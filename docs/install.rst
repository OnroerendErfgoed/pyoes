===========
Installatie
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

Om te starten, kun je best gebruik maken van de pyoes scaffold. Deze zal de 
standaard bestanden die nodig zijn toevoegen aan een static dir. Op zich is dit
geen volledige pyramid scaffold. Deze maakt dus geen models, views en andere aan. 
Gebruik hiervoor een andere scaffold zoals de alchemy scaffold.

.. code-block:: bash

    $ pcreate -s alchemy <package_naam>
    $ pcreate -s pyoes <package_naam>

Vooraleer verder te gaan, moet je zorgen dat compass en best ook foundation 
aanwezig zijn op je systeem.

.. code-block:: bash

    $ [sudo] apt-get install rubygems   
    $ [sudo] gem install zurb-foundation 
    $ [sudo] gem install compass

:mod:`pyoes` komt met een set van :term:`Jinja2` templates. Om deze te kunnen gebruiken, 
moet je wel nog de parameter jinja2.directories correct instellen. Daarnaast 
zijn er ook nog filters die je kunt toevoegen aan je project.

Tenslotte moet je ook aangeven waar je compass extensions dir staat.

.. code-block:: ini

    jinja2.directories = 
        <package_name>:templates
        pyoes:templates
    jinja2.filters = 
        setattr = pyoes.utils.set_attr_filter

    # Is nodig voor het install_compass_extension script
    compass.extensions_dir = %(here)s/<package_name>/static/extensions

Kopieer nu een aantal bestanden uit de pyoes package naar je lokale omgeving.

.. code-block:: bash

    $ install_compass_extensions development.ini

Installeer nu de compass extension in je static dir.

.. code-block:: bash

    $ cd static
    $ compass install pyoes

Er zijn een aantal statische files nodig die meegeleverd worden met :mod:`pyoes`. 
Om deze te kunnen gebruiken moeten je een static view registeren.

.. code-block:: python

    config.add_static_view('pyoes_static', 'pyoes:static')

Update
======

Als er nieuwe versies van :mod:`pyoes` zijn, moet je niet alle bovenstaande 
stappen terug uitvoeren. Zo is het normaal niet nodig om de scaffold nogmaals 
uit te voeren. Je kunt wel eens controleren of er wijzigingen in de scaffold 
zijn aangebracht.

.. code-block:: bash

    $ pcreate -s pyoes <package_name> --simulate

Indien er relevante wijzigingen zijn, kun je bestand per bestand beslissen wat
er gedaan moet worden.

.. code-block:: bash

    $ pcreate -s pyoes <package_name> --interactive

De :term:`Jinja2` templates zijn automatisch beschikbaar. Als er nieuwe filters zijn 
toegevoegd, moet je deze wel nog toevoegen aan je `.ini` bestand.

Wat je zeker niet mag vergeten is om de compass extension uit de virtualenv te
kopiëren naar je compass extensions dir.

.. code-block:: bash

    $ install_compass_extensions development.ini
