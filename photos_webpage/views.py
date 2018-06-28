from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Photos'}


@view_config(route_name= 'galery', renderer='templates/galery.jinja2')
def galery(request):
    return {'project': 'Photos'}

@view_config(route_name='update', renderer='templates/update.jinja2')
def update(request):
    return {'project': 'Photos'}

@view_config(route_name='select', renderer='templates/select.jinja2')
def select(request):
    return {'project': 'Photos'}