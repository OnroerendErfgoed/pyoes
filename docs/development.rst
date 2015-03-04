Ontwikkeling
============

Deze bibliotheek is nog vrij nieuw en zal vrij veel wijzigen. Aangezien het hier
eerder om visuele elementen gaat dan code, is het aantal unit tests eerder
bescheiden.

Nieuwe features worden uitgewerkt in een feature branch in :term:`git`
en dan via een pull-request in :term:`Github` gemerged met de master.


unit tests
----------

Zoals altijd bij een bibliotheek proberen we zo goed mogelijk de code te testen. 
Om het ontwikkelen en testen makkelijk te maken werken we met tox. Via tox zal 
de code getest worden op python 2.7, 3.3 en 3.4. Er wordt ook code coverage
berekend op basis van python 2.7.

Tox moet aanwezig zijn in je globale python installatie. Indien dit nog niet zo 
is, kan je het simpel installeren:

.. code-block:: bash

    $ pip install tox

De uiteindelijke unit tests voer je uit door in de root van de repository te 
gaan staan (de map waarin :file:`tox.ini` staat) en het tox commando uit te 
voeren:

.. code-block:: bash
    
    $ tox

Indien je aan het ontwikkelen bent kan het uitvoeren van alle tests (en vooral
het opbouwen van de omgevingen) soms wat lang duren. Je kunt ook aangeven dat je
enkel de tests van een enkele omgeving wenst uit te voeren:

.. code-block:: bash

    # Enkel de python 2.7 tests uitvoeren
    $ tox -e py27
    # Enkel de coverage tests uitvoeren
    $ tox -e cover
