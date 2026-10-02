from pyramid.scaffolds import PyramidTemplate


class PyoesTemplate(PyramidTemplate):
    _template_dir = "pyoes_scaffold"
    summary = (
        "Een scaffold om een pyramid project uit te breiden met de OE stijl "
        "(Webuniversum via pyoes-wu) en de bijhorende jinja2 templates."
    )


class PyoesAdminTemplate(PyramidTemplate):
    _template_dir = "pyoes_admin_scaffold"
    summary = (
        "Een scaffold om de admin interface van een pyramid project uit te "
        "breiden met OE stijl bestanden op basis van sass (foundation, "
        "deprecated)."
    )


class PyoesProcesTemplate(PyramidTemplate):
    _template_dir = "pyoes_proces_scaffold"
    summary = (
        "Een scaffold om de proces interface van een pyramid project uit te "
        "breiden met OE stijl bestanden op basis van sass (foundation, "
        "deprecated)."
    )
