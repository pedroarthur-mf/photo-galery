from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Photos'}


@view_config(route_name= 'galery', renderer='templates/galery.jinja2')
def galery(request):
    return {'project': 'Photos'}

@view_config(route_name='update',
             request_method='POST',
             renderer='templates/update.jinja2')
def update_photo(request):
    file = request.params.get('photo', '')
    request.storage.save(request.POST['photo'], replace=True)
    print HTTPSeeOther(request.route_url('update'))
    return HTTPSeeOther(request.route_url('update'))


@view_config(route_name='update', renderer='templates/update.jinja2')
def update_page(request):
    return {'project': 'Photos'}

@view_config(route_name='select', renderer='templates/select.jinja2')
def select(request):
    return {'project': 'Photos'}