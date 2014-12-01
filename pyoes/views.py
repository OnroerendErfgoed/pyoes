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

@view_config(route_name='beeldbank', renderer='templates/beeldbank.jinja2')
def beeldbank(request):
    return {}

@view_config(route_name='beeldbank-detail', renderer='templates/beeldbank-detail.jinja2')
def beeldbank_detail(request):
    return {}

@view_config(route_name='inventaris', renderer='templates/inventaris.jinja2')
def inventaris(request):
    return {}