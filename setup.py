import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_jinja2',
    ]

setup(name='pyoes',
      version='0.1.0a1',
      description='Algemene onroerenderfgoed stijl voor pyramid',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Koen Van Daele',
      author_email='koen.vandael@rwo.vlaanderen.be',
      url='',
      keywords='pyramid sass compass style css jinja2 templates',
      packages=find_packages(),
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
      [console_scripts]
      install_compass_extensions = pyoes.scripts.install_compass_extensions:main
      """,
      )
