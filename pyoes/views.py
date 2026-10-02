from pyramid.view import view_config


@view_config(route_name="home", renderer="templates/index.jinja2")
def home(request):
    return {}


@view_config(route_name="burgerprofiel", renderer="templates/burgerprofiel.jinja2")
def header_footer(request):
    return {}


@view_config(route_name="burgerprofiel2", renderer="templates/burgerprofiel2.jinja2")
def header_footer2(request):
    return {}


@view_config(route_name="headerlinks", renderer="templates/headerlinks.jinja2")
def headerlinks(request):
    return {}


@view_config(route_name="navigation", renderer="templates/navigation.jinja2")
def navigation(request):
    return {}


@view_config(route_name="401", renderer="templates/401.jinja2")
def error401(request):
    return {}


@view_config(route_name="403", renderer="templates/403.jinja2")
def error403(request):
    return {}


@view_config(route_name="404", renderer="templates/404.jinja2")
def error404(request):
    return {}


@view_config(route_name="500", renderer="templates/500.jinja2")
def error500(request):
    return {}
