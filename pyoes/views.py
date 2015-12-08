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

@view_config(route_name='besluitendatabank', renderer='templates/besluitendatabank.jinja2')
def besluitendatabank(request):
    return {}

@view_config(route_name='beheersplannen', renderer='templates/beheersplannen.jinja2')
def beheersplannen(request):
    return {}

@view_config(route_name='beheersplannenres', renderer='templates/beheersplannen/result.jinja2')
def beheersplannenres(request):
    return {}

@view_config(route_name='actorenfront', renderer='templates/actorenfront.jinja2')
def actorenfront(request):
    return {}

@view_config(route_name='detail-bedrijf', renderer='templates/actorenfront/detail-bedrijf.jinja2')
def actorenfrontdetailbedrijf(request):
    return {}

@view_config(route_name='detail-bedrijfv2', renderer='templates/actorenfront/detail-bedrijfv2.jinja2')
def actorenfrontdetailbedrijfv2(request):
    return {}

@view_config(route_name='detail', renderer='templates/actorenfront/detail.jinja2')
def actorenfrontdetail(request):
    return {}

@view_config(route_name='actorenzoek', renderer='templates/actorenzoek.jinja2')
def actorenzoek(request):
    return {}

@view_config(route_name='actorenzoekdetail', renderer='templates/actorenzoek/detail.jinja2')
def actorenzoekdetail(request):
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

@view_config(route_name='postregistratie', renderer='templates/postregistratie/index.jinja2')
def postregistratie(request):
    return {}

@view_config(route_name='postreg-aanmaken', renderer='templates/postregistratie/aanmaken.jinja2')
def postreg_aanmaken(request):
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

@view_config(route_name='401', renderer='templates/401.jinja2')
def viernuleen(request):
    return {}

@view_config(route_name='403', renderer='templates/403.jinja2')
def viernuldrie(request):
    return {}

@view_config(route_name='404', renderer='templates/404.jinja2')
def viernulvier(request):
    return {}

@view_config(route_name='500', renderer='templates/500.jinja2')
def vijfhonderd(request):
    return {}

@view_config(route_name='atramhasismenu', renderer='templates/atramhasis_menu.jinja2')
def atramhasismenu(request):
    return {}