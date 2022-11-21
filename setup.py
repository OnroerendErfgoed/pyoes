# -*- coding: utf-8 -*-

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'python-dateutil',
    ]

setup(name='pyoes',
      version='0.15.0',
      description='Algemene onroerenderfgoed stijl (gebaseerd op de Vlaamse huisstijl) voor pyramid',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: JavaScript",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Text Processing :: Markup :: HTML"
        ],
      author='Koen Van Daele',
      author_email='koen.vandaele@vlaanderen.be',
      url='https://pyoes.readthedocs.org/en/latest/',
      keywords='pyramid oe onroerend erfgoed sass compass style css jinja2 templates',
      packages=['pyoes'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyoes",
      entry_points="""\
      [paste.app_factory]
      main = pyoes:main
      [pyramid.scaffold]
      pyoes=pyoes.scaffolds:PyoesTemplate
      pyoesAdmin=pyoes.scaffolds:PyoesAdminTemplate
      pyoesProces=pyoes.scaffolds:PyoesProcesTemplate
      """,
      )
