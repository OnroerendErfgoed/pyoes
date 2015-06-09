0.4.2 (09-06-2015)
==================

* Kleine layout fixes
* Admin interface update

0.4.1 (29-05-2015)
==================
* Toevoegen van een textarea element met een inline label 
* Toevoegen van een checkbox met een placeholder
* Toevoegen van een generieke profile template
* Toevoegen van een macro om een URI voor een resource te genereren
* Toevoegen van een generiek datetime format filter
* Opkuisen van het project
* Schrijven van nieuwe tests om coverage te vergroten

0.4.0 (24-04-2015)
==================

* fix voor favicon
* Speciale input velden toegevoegd
* Voorbeeldtemplates verder uitgewerkt
* Generieke 404/500 templates toegevoegd
* Alertblock toegevoegd
* Mediaqueries toegevoegd die problemen met header op mobile devices oplost
* Problemen met footer verholpen

0.3.3 (04-03-2015)
==================
* Fix voor gebruikersnamen
* Documentatie geüpdate ivm admin scaffold

0.3.2 (26-02-2015)
==================
* Aanpassingen vooral aan admin scaffold


0.3.1 (23-02-2015)
==================

* Admin scaffold toegevoegd
* Aanmelden/Afmelden knop toegevoegd
* Google analytics geüpdate naar Universal analytics
* Font-awesome toegevoegd als bower dependency

0.3.0 (12-02-2015)
==================

* Erfgoedstijl aangepast aan vereisten van de nieuwe Vlaamse Huisstijl


0.2.1 (25-11-2014)
==================

* Released as open source on PyPI.
* Copyright date can be changed again. Now works with a variable instead of 
  a block.

0.2.0 (14-08-2014)
==================

* Andere manier van omgaan met Foundation dependency. Gaat nu via bower.
* Upgraden naar Foundation 5.3.x. Bower zal steeds de laatste versie in de 5.3
  reeks proberen aan te houden.
* Toevoegen van Foundation Icon Fonts 3
* Unit tests naar py.test ipv nose.
* Basistemplate is nu meer responsive dan vroeger.
* Standaard breedte van de css grid werd nu gelijk geschakeld met die van de
  corporate site.
* Footer werd gewijzigd zodat er blauw over de ganse breedte is.

0.1.1 (06-08-2014)
==================

* Toevoegen van een mogelijkheid om css_files in de html header te injecteren. (#7) [JonathanGeosolutions]
* Toevoegen van een mogelijkheid om de HTML header te overriden in een template.
* Testen ook laten uitvoeren op py33 en py34.

0.1.0
=====

* Eerste stabiele release.
* Maakt nu gebruik van onze eigen typekit code.

0.1.0b2
=======

* Terug naar TypeKit. Voorlopig gebruiken we de account van Glue. Op een bepaald
  moment zal iemand wel eens voor onze eigen accout moeten betalen.

0.1.0b1
=======

* Extra documentatie met sphinx. (#5)
* Static files zoals favicon en robots.txt kunnen geleverd worden door pyoes. (#6)
* Niet meer nodig om pyoes:static view te includen. Vanaf nu moet pyoes zelf 
  wel geinclude worden, deze handelt dan de rest af.
* De scaffold zal meteen een sass bestand voor de applicatie specifieke css
  aanmaken.

0.1.0a3
=======

* Overschakelen op open fonts. (#4)
* Js files kunnen doorgegeven worden door extended templates. (#3)
* Verwijderen van een onbestaande dit in het install_compass_extensions script werkt. (#1)
* Docs wat uitgebreid. (#2)
* Layout van de breadcrumbs wat compacter gemaakt.

0.1.0a2
=======

* Zorgend dat jquery protocol onafhankelijk kan geladen worden. Gaf problemen 
  op https sites.

0.1.0a1
=======

* eerste versie die getagged wordt
* aantal jinja2 templates
* sass files
* nog zeer onvolledig en met gebrekkige documentatie
