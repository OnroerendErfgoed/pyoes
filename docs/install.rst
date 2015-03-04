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
        'pyoes'
    ]

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

Om te starten, kun je best gebruik maken van de pyoes scaffold. Deze zal de
standaard bestanden die nodig zijn toevoegen aan een static dir. Op zich is dit
geen volledige pyramid scaffold. Deze maakt dus geen models, views en andere aan. 
Gebruik hiervoor een andere scaffold zoals de alchemy scaffold. Er zijn 2 scaffolds beschikbaar in pyoes:
* een scaffold voor de public frontend (pyoes)
* een admin scffold (pyoesAdmin)
De admin scaffold is nieuw vanaf versie 3.1.

.. code-block:: bash

    $ pcreate -s alchemy <package_naam>
    $ pcreate -s pyoes <package_naam>
    # of
    $ pcreate -s pyoesAdmin <package_naam>

.. warning::

   Voer deze commando's niet uit van in de folder waarin je code staat, maar
   vanuit de bovenliggende folder. Dus, als je je git repository hebt
   uitgecheckt naar :file:`/home/me/projects/my_app`, voer het commando dan
   uit in de folder :file:`/home/me/projects`.

Vooraleer verder te gaan, moet je zorgen dat compass en bower aanwezig zijn op je systeem.

.. code-block:: bash
    
    # ruby 1.9+
    $ [sudo] apt-get install ruby-dev
    $ [sudo] gem install compass
    $ [sudo] npm install -g bower grunt-cli

Deze kunnen ook via `Bundler <http://bundler.io/>`__ geïnstalleerd worden met de resources die in
:file:`Gemfile` staan.

.. code-block:: bash

    $ cd pyoes/static
    $ bundle install

:mod:`pyoes` komt met een set van :term:`Jinja2` templates. Om deze te kunnen gebruiken, 
moet je wel nog de parameter jinja2.directories correct instellen. Daarnaast 
zijn er ook nog filters die je kunt toevoegen aan je project.

.. code-block:: ini

    jinja2.directories =
        <package_name>:templates
        pyoes:templates
    jinja2.filters = 
        setattr = pyoes.utils.set_attr_filter

Installeer foundation en font-awesome nu lokaal via bower.

.. code-block:: bash

    $ cd pyoes/static
    $ bower install

Tenslotten moet je :mod:`pyoes` toevoegen aan je main functie. Dit zorgt er voor
dat de correcte static dir wordt toegevoegd en dat een aantal static views 
geregistreerd worden.

.. code-block:: python

    config.include('pyoes')



Update
======

Als er nieuwe versies van :mod:`pyoes` zijn, moet je niet alle bovenstaande 
stappen terug uitvoeren. Je kunt gewoon de scaffold terug uitvoeren en deze
zal de nodige bestanden terug kopiëren.

Je kunt op voorhand nagaan wat de wijzigingen zullen zijn door het commando
te simuleren.

.. code-block:: bash

    $ pcreate -s pyoes <package_name> --simulate

Indien er relevante wijzigingen zijn, kun je bestand per bestand beslissen wat
er gedaan moet worden.

.. code-block:: bash

    $ pcreate -s pyoes <package_name> --interactive

De :term:`Jinja2` templates zijn automatisch beschikbaar. Als er nieuwe filters zijn 
toegevoegd, moet je deze wel nog toevoegen aan je `.ini` bestand.

Van versie 1.x naar 2.x
-----------------------


.. warning::

    Bij de update van 1.x naar 2.x zijn er vrij significante wijzigingen doorgevoerd
    in de organisatie van de bestanden. Het is dus best erg voorzichtig te zijn
    bij deze update. Indien er zware wijzigingen zijn doorgevoerd, zullen er conflicten
    optreden. Het is best deze update op voorhand goed te simuleren en interactief
    uit te voeren.

Volgende bestanden zullen gewijzigd worden.

 * :file:`static/css/app.css`: Is sowieso het resultaat van een 
   :command:`compass compile` operatie en moet dus gehergenereerd worden op 
   basis van je eigen sass code.
 * :file:`static/config.rb`: Mag gewoon vervangen worden en kan geen kwaad.
 * :file:`templates/layout.jinja2`: Er wordt een starttemplate meegeleverd voor
   nieuwe scaffolds. Bij een update is het meestal best deze te laten zoals
   ze is. Je moet wel zorgen dat de declaratie van een `app_package` correct
   wordt ingesteld in je eigen :file:`templates/layout.jinja2`.

Na de update mogen volgende bestanden in de :file:`static` folder verwijderd worden:

 * :file:`css/fonts`: We maken nu gebruik van de foundation icon fonts.
 * :file:`js/foundation` en :file:`js/vendor`: Worden nu uit 
   :file:`bower_components` geladen. Indien nodig kan je hier libraries toevoegen.
 * :file:`sass`: Deze volledige folder wordt vervangen door een :file:`scss`
   folder. Voor je deze folder verwijderd, controleer je best of je hier in
   :file:`sass/{+package+}/_{+package+}.scss` eigen wijzigingen hebt aangebracht.
   Indien dat zo is, dien je deze over te brengen naar 
   :file:`scss/_{+package+}.scss`.
 * :file:`extensions`: Werd aangemaakt door :command:`compass` en is nu overbodig.
 * :file:`img/icons`, :file:`img/pinpoints` en andere bestanden: Alle bestanden
   werden verplaatst naar :file:`img/pyoes`. Alles buiten deze folder dat je niet
   zelf hebt toegevoegd, mag weg.


Van versie 2.x naar 3.x
-----------------------

.. warning::

    Bij de update van 2.x naar 3.x zijn er vrij significante wijzigingen doorgevoerd
    in de organisatie van de bestanden. Het is dus best erg voorzichtig te zijn
    bij deze update. Indien er zware wijzigingen zijn doorgevoerd, zullen er conflicten
    optreden. Het is best deze update op voorhand goed te simuleren en interactief
    uit te voeren.