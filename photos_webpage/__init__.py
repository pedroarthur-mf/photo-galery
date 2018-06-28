from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_storage.s3')
    config.add_static_view('static', 'static', cache_max_age=3600)
   
    config.add_route('home', '/')

    config.add_route('update', '/update')
    config.add_route('select', '/select')
    config.add_route('galery', '/galery')


    config.scan()
    return config.make_wsgi_app()
