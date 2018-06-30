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
