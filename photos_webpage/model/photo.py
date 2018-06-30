class Photo(object):

    def __init__(self, name, url, visible=False):
        self._id = None
        self._name = name
        self._url = url
        self._visible = visible


    def __str__(self):
        return self._name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
