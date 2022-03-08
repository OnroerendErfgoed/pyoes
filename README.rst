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

More information about this library can be found in the docs `folder`. These can
be build using `Sphinx <http://sphinx-doc.org>`_.

.. code-block:: bash

    # activate your virtual env
    $ pip install -r requirements-dev.txt
    $ cd docs
    $ make html
    # You can also build a pdf, provided you have the correct latex toolchain installed.
    $ make latexpdf
