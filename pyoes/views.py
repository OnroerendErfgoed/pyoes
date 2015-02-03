from pyramid.view import view_config


@view_config(route_name='index', renderer='templates/index.jinja2')
def home(request):
    return {}

@view_config(route_name='header-footer', renderer='templates/header-footer.jinja2')
def header_footer(request):
    return {}

@view_config(route_name='grids', renderer='templates/grids.jinja2')
def grids(request):
    return {}

@view_config(route_name='beeldbank', renderer='templates/beeldbank/beeldbank.jinja2')
def beeldbank(request):
    return {}

@view_config(route_name='beeldbank-detail', renderer='templates/beeldbank/beeldbank-detail.jinja2')
def beeldbank_detail(request):
    return {}

@view_config(route_name='beeldbank-zoeken', renderer='templates/beeldbank/beeldbank-uitgebreid-zoeken.jinja2')
def beeldbank_zoeken(request):
    return {}

@view_config(route_name='inventaris', renderer='templates/inventaris/inventaris.jinja2')
def inventaris(request):
    return {}

@view_config(route_name='inventaris-article', renderer='templates/inventaris/inventaris-article.jinja2')
def inventaris_article(request):
    return {}

@view_config(route_name='inventaris-articleID', renderer='templates/inventaris/inventaris-articleID.jinja2')
def inventaris_articleID(request):
    return {}

@view_config(route_name='inventaris-articleIDv2', renderer='templates/inventaris/inventaris-articleIDv2.jinja2')
def inventaris_articleIDv2(request):
    return {}

@view_config(route_name='inventaris-articleIDfull', renderer='templates/inventaris/inventaris-articleIDfull.jinja2')
def inventaris_articleIDfull(request):
    return {}

@view_config(route_name='inventaris-articleIDfullv2', renderer='templates/inventaris/inventaris-articleIDfullv2.jinja2')
def inventaris_articleIDfullv2(request):
    return {}

@view_config(route_name='inventaris-articleIDfullv3', renderer='templates/inventaris/inventaris-articleIDfullv3.jinja2')
def inventaris_articleIDfullv3(request):
    return {}

@view_config(route_name='inventaris-zoekoverzicht', renderer='templates/inventaris/inventaris-zoekoverzicht.jinja2')
def inventaris_zoekoverzicht(request):
    return {}

@view_config(route_name='icons', renderer='templates/icons.jinja2')
def icons(request):
    return {}

@view_config(route_name='blokken', renderer='templates/blokken.jinja2')
def blokken(request):
    return {}

@view_config(route_name='typo', renderer='templates/typo.jinja2')
def typo(request):
    return {}

@view_config(route_name='navigation', renderer='templates/navigation.jinja2')
def navigation(request):
    return {}

@view_config(route_name='colors', renderer='templates/colors.jinja2')
def colors(request):
    return {}

@view_config(route_name='elements', renderer='templates/elements.jinja2')
def elements(request):
    return {}

@view_config(route_name='images', renderer='templates/images.jinja2')
def images(request):
    return {}

@view_config(route_name='article', renderer='templates/article.jinja2')
def article(request):
    return {}

@view_config(route_name='article9-3', renderer='templates/article9-3.jinja2')
def article93(request):
    return {}

@view_config(route_name='geoportaal', renderer='templates/geoportaal/geoportaal.jinja2')
def geoportaal(request):
    return {}

@view_config(route_name='pinpoints', renderer='templates/pinpoints.jinja2')
def pinpoints(request):
    return {}