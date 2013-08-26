import os
import sys
import shutil

import pyoes

from pyramid.paster import (
    get_appsettings,
)

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)

    config_uri = argv[1]
    settings = get_appsettings(config_uri)

    if not 'compass.extensions_dir' in settings:
        print('Er is geen compass.extensions_dir opgegeven in de settings file.')
        sys.exit(1)

    pyoes_dir = os.path.dirname(pyoes.__file__)

    pyoes_ext = os.path.join(pyoes_dir, 'static', 'extensions', 'pyoes')

    dst = os.path.join(settings['compass.extensions_dir'],'pyoes')

    shutil.rmtree(dst, True)

    shutil.copytree(pyoes_ext, dst)

    print ('pyoes werd aangemaakt in %s' % dst)
