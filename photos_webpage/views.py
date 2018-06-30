# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther

from .functions.photos import *

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'page_title': 'Photos'}


@view_config(route_name= 'galery', renderer='templates/galery.jinja2')
def galery(request):
    functions = PhotosFunction()
    return {
        'page_title': 'Galeria',
        'photos' : functions.list()
    }

@view_config(route_name='update',
             request_method='POST',
             renderer='templates/update.jinja2')
def update_photo(request):
    file_name = request.storage.save(request.POST['photo'], randomize=True)
    url = "https://s3-sa-east-1.amazonaws.com/photosprojecttest/" + request.storage.url(file_name)
    print "url: " + url

    functions = PhotosFunction()
    functions.insert(file_name, url)
    return HTTPSeeOther(request.route_url('update'))


@view_config(route_name='update', renderer='templates/update.jinja2')
def update(request):
    return {'page_title': 'Photos Uploaded'}

@view_config(route_name='select', renderer='templates/select.jinja2')
def select(page_title):
    functions = PhotosFunction()
    return {
        'page_title': 'Photos',
        'photos' : functions.list()
    }