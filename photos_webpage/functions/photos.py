# -*- coding: utf-8 -*-
from bson import ObjectId

from ..database.mongo_database import *
from ..model.photo import Photo

class PhotosFunction():
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, file_name, url): 
        photo_to_insert = {
            "name": file_name,
            "url": url,
            "visible": False
        }
        return self.db.photos.insert(photo_to_insert)

    def update_visible(self, visibles):
        all_photos = self.list()
        print type(visibles)
        # print visibles
        for photo in all_photos:
            print photo.name
            if photo.name in visibles['visible']:
                # print 'entrei'
                # print photo.visible
                if photo.visible != True:
                    query = query = {'_id': ObjectId(photo.id)}
                    update = {'name': photo.name, 'url': photo.url, 'visible': True}
                    self.db.photos.update(query, update)
            else:
                if photo.visible == True:
                    query = query = {'_id': ObjectId(photo.id)}
                    update = {'name': photo.name, 'url': photo.url, 'visible': False}
                    self.db.photos.update(query, update)


    def get(self,query):
        photos = list(self.db.photos.find(query))
        if photos:
            photo_list = []
            for p in photos:
                photo = Photo(
                    p.get('name',''),
                    p.get('url',''),
                    p.get('visible', True)
                )
                photo.id = p.get('_id', '')
                photo_list.append(photo)
            return photo_list
        return []

    def list(self):
        return self.get({})
