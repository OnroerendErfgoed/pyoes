=======
Gebruik
=======

CSS bewerken
============

Als je aan css werkt is het best om compass je files te laten monitoren zodat 
deze wanneer nodig kan hercompileren.

.. code-block:: bash
    
    $ cd static
    $ compass watch .
    # je kunt ook gewoon eenmalig compileren
    $ compass compile

Maak je eigen .scss file aan in :file:`/<package_name>/static/sass/<package_name>/_<package_name>.scss`. 
De underscore aan het begint zorgt er voor dat dit bestand als een plugin
gezien wordt en niet afzonderlijk gecompileerd wordt.

Als je met compass watch werkt, dan zal telkens je een bestand wijzigt je 
:file:`app.css` bestand opnieuw worden aangemaakt. Alhoewel we deze compilatie
ook bij het deployen zouden kunnen uitvoeren, zou dit weer tot extra build-time
dependencies leiden. Vergeet daarom zeker niet om telkens je :file:`app.css` 
bestand in te checken.

Jinja2 templates
================

:mod:`pyoes` levert een een globale layout :file:`pyoes/layout.jinja2` die 
vooral een algemene header en footer levert. In deze layout zijn er een aantal
blocks gedefinieerd die in andere templates kunnen overschreven worden.

Idealiter maak je een eigen :file:`layout.jinja2` aan waarin je een aantal 
zaken instelt die voor de ganse site van tel zijn. 

.. code-block:: jinja

    {% extends "pyoes/layout.jinja2" %}

    {% set ga_key = request.registry.settings["ga.tracker_key"] %}

    {% set top_nav = [
        ('Over deze site', request.route_path('home')),
        ('Contact', request.route_path('contact'))
    ]
    -%}

    {% set footer_nav = [
        ('Toegankelijkheid', 'https://www.onroerenderfgoed.be/toegankelijkheid'), 
        ('Juridische Informatie', 'https://www.onroerenderfgoed.be/juridische-informatie'),
    ]
    -%}

    {% set zoeken_action = request.route_path('zoeken') %}
    {% set zoeken_placeholder = 'Zoek iets op deze sites...' %}

    {% block app_css %}{{request.static_path('<package_name>:static/css/app.css')}}{% endblock %}

In je individuele templates kun je dan weer erven van je eigen layout zodat
je indien nodig wijzigingen kunt aanbrengen die over de ganse site werken.

.. code-block:: jinja

    {% extends "layout.jinja2" %}

    {% block content %}

    <section class="inhoud">
        <div class="row">
            <div class="large-3 columns">
                <nav>
                    <h2>Een submenu of zo</h2>
                    ...
                </nav>
            </div>

            <div class="large-9 columns">

                <h1>Over deze site</h1>

                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque hendrerit condimentum sollicitudin. Curabitur molestie, dui vel ultricies facilisis, eros nulla bibendum erat, ut viverra elit ligula eget lectus. Donec et nibh eget ipsum porta dapibus. Curabitur placerat dapibus lacus sed gravida. Nulla tempor fermentum nibh ut porttitor. Pellentesque malesuada faucibus ante a eleifend. Donec feugiat felis ullamcorper enim aliquet laoreet. Praesent sodales gravida fermentum. Praesent condimentum sollicitudin libero, ac malesuada ligula cursus non. Nullam nisi neque, fermentum sit amet pretium condimentum, bibendum ac augue. Vivamus ornare tristique dolor sit amet suscipit. Aliquam aliquam arcu vel neque sollicitudin blandit. Praesent vitae urna sit amet ligula rutrum adipiscing sed quis erat. Suspendisse potenti. Nam erat sem, tincidunt id scelerisque ut, dignissim id mi.</p>

                <p>Nullam ultricies consectetur quam nec sagittis. Aenean ultricies vulputate nunc hendrerit pharetra. Nam in lacus leo, ut sodales metus. Nulla nisl dolor, condimentum vel pulvinar vel, lobortis ut enim. Sed laoreet rutrum ligula quis dictum. Vivamus at sem at metus ullamcorper porta. Ut orci orci, sollicitudin ac fringilla et, tempus vel velit. Curabitur non quam sit amet tellus placerat consectetur. Duis congue consectetur faucibus. Maecenas tempor feugiat consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent consequat sapien sit amet est pellentesque laoreet. Cras ullamcorper nisl et ipsum iaculis vel rutrum urna consectetur. Fusce mauris leo, tempus non rutrum eget, faucibus ac lorem. Aliquam eget erat tincidunt enim feugiat facilisis. Donec id sapien at mi molestie semper.</p>

                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mauris nibh, egestas in vehicula vitae, dignissim a dui. Nam at augue mauris, eu vulputate lectus. Vivamus vulputate viverra dolor, ornare pharetra purus vehicula ut. Fusce lobortis, est feugiat pretium adipiscing, tortor orci porta orci, vel malesuada leo ligula nec ante. Vestibulum urna leo, varius vel adipiscing luctus, porta sit amet mi. Vivamus quis urna vitae nisi mollis feugiat vel in libero.</p>
            </div>
        </div>
    </section>
    {% endblock %}

demonstratie
============

Als je gewoon eens de nieuwe stijl wenst te bekijken en een overzicht van de 
mogelijkheden wil krijgen, kun je best de demo toepassing installeren.

.. code-block:: bash

    $ git clone https://github.com/OnroerendErfgoed/pyoes pyoes_demo
    $ cd pyoes_demo
    $ mkvirtualenv pyoes_demo
    $ python setup.py install

Om het makkelijk te maken om de demo-toepassing te draaien naast een toepassing
die je aan het ontwikkelen bent, draait deze op poort `6555` en niet op poort 
`6543`.

.. code-block:: bash

    $ pserve development.ini

Deze toepassing heeft een aantal eigen templates en stylesheets die als 
inspiratie kunnen dienen. De templates kun je vinden in :file:`pyoes/templates`, 
dit in tegenstelling tot de algemene pyoes templates die door een andere 
applicatie worden overgenomen. Deze kun je vinden in :file:`pyoes/templates/pyoes`.

De :file:`pyoes/static` folder bevat de scss bestanden van deze toepassing en 
nog een aantal oude referentiebestanden van glue en andere pogingen.
