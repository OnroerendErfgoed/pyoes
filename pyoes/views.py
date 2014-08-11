from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}

@view_config(route_name='vinden', renderer='templates/vinden.jinja2')
def vinden(request):
    return {}

@view_config(route_name='pinpoints', renderer='templates/pinpoints.jinja2')
def pinpoints(request):
    return {}

@view_config(route_name='icons', renderer='templates/icons.jinja2')
def icons(request):
    return {}
