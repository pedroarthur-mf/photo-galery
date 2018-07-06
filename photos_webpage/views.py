# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther

from .functions.photos import *

# @view_config(route_name='home', renderer='templates/mytemplate.jinja2')
# def my_view(request):
#     return {'page_title': 'Photos'}

@view_config(route_name= 'galery', renderer='templates/galery.jinja2')
def galery(request):
    functions = PhotosFunction()
    # Caso não tenha foto mostrar mensagem*******
    return {
        'page_title': 'Galeria',
        'photos' : functions.get({"visible": True})
    }

@view_config(route_name='update',
             request_method='POST',
             renderer='templates/update.jinja2')
def update_photo(request):
    file_name = request.storage.save(request.POST['photo'], randomize=True)
    url = "https://s3-sa-east-1.amazonaws.com/<name of your bucket>/" + request.storage.url(file_name)
    functions = PhotosFunction()
    functions.insert(file_name, url)
    return {'page_title': 'Update',
            'result': 'Foto Enviada com sucesso'}

@view_config(route_name='update', renderer='templates/update.jinja2')
def update(request):
    return {'page_title': "Update"}

@view_config(route_name='select', renderer='templates/select.jinja2')
def select(request):
    functions = PhotosFunction()
    return {
        'page_title': 'Selecao',
        'photos': functions.list()
    }

@view_config(route_name='select',
             request_method='POST',
             renderer='templates/galery.jinja2')
def select_update(request):
    functions = PhotosFunction()
    params = request.params
    visibles = params.getall('visible')
    print 'visibles:'
    print visibles
    functions.update_visible(params.dict_of_lists())
    return {
        'page_title': 'Galeria',
        'photos' : functions.get({"visible": True})
    }