from paste.httpserver import serve
from pyramid.config import Configurator

from pwc.views import make_request, index

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'pwc:static', cache_max_age=3600)
    config.add_route('request', '/request')
    config.add_view(make_request, route_name='request', renderer="json")
    config.add_route('index', '/')
    config.add_view(index, route_name='index', renderer='pwc.mako')
    return config.make_wsgi_app()