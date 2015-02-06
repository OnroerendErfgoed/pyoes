from pyramid.scaffolds import PyramidTemplate

class PyoesTemplate(PyramidTemplate):
    _template_dir = 'pyoes_scaffold'
    summary = 'Een scaffold om een pyramid project uit te breiden met OE stijl\
    bestanden op basis van sass en compass.'


class Pyoes030Template(PyramidTemplate):
    _template_dir = 'pyoes_0.3.0'
    summary = 'Een scaffold om een pyramid project uit te breiden met OE stijl\
    bestanden op basis van sass en compass.'