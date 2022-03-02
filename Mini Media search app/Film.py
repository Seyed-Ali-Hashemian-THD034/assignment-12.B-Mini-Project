#class media_Film
from Media import Media

class Film(Media):
    def __init__(self,Media):
        Media.__init__(self, Media[0], Media[1], Media[2], Media[3], Media[4], Media[5], Media[6])

