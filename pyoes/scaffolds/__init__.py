from pyramid.scaffolds import PyramidTemplate

class PyoesTemplate(PyramidTemplate):
    _template_dir = 'pyoes_scaffold'
    summary = 'Een scaffold om een pyramid project uit te breiden met OE stijl\
    bestanden op basis van sass en compass.'


class PyoesAdminTemplate(PyramidTemplate):
    _template_dir = 'pyoes_admin_scaffold'
    summary = 'Een scaffold om een de admin interface van een pyramid project uit te breiden met OE stijl\
    bestanden op basis van sass en compass.'


class PyoesProcesTemplate(PyramidTemplate):
    _template_dir = 'pyoes_proces_scaffold'
    summary = 'Een scaffold om een de proces interface van een pyramid project uit te breiden met OE stijl\
    bestanden op basis van sass en compass.'