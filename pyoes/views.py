from pyramid.view import view_config


@view_config(route_name="home", renderer="templates/index.jinja2")
def home(request):
    return {}


@view_config(route_name="typo", renderer="templates/typo.jinja2")
def typo(request):
    return {}


@view_config(route_name="article", renderer="templates/article.jinja2")
def article(request):
    return {}


@view_config(route_name="401", renderer="templates/401.jinja2")
def viernuleen(request):
    return {}


@view_config(route_name="403", renderer="templates/403.jinja2")
def viernuldrie(request):
    return {}


@view_config(route_name="404", renderer="templates/404.jinja2")
def viernulvier(request):
    return {}


@view_config(route_name="500", renderer="templates/500.jinja2")
def vijfhonderd(request):
    return {}
