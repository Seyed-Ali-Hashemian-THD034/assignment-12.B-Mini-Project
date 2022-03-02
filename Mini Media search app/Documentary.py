#class media_Documentary
from Media import Media

class  Documentary(Media) :
    def __init__(self,Media):
        Media.__init__(self, Media[0], Media[1], Media[2], Media[3], Media[4], Media[6])
