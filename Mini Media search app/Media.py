#class media
from os import name


class Media :
    def __init__(self, id, n, i, di, du, c, u):
        self.id = id
        self.name = n
        self.IMDB_score = i
        self.director = di                    # آدرس سایت پخش کننده فیلم 
        self.duration = du
        self.casts = c
        self.url = u
