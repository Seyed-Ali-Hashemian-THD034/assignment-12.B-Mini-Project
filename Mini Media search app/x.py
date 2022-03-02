#class media - properties
class media :
    def __init__(self, n, di, i, u, du, c):
        self.name = n
        self.director = di
        self.IMDB_score = i
        self.url= u                    # آدرس سایت پخش کننده فیلم 
        self.duration= du
        self.casts= c


class clip(media) :
    def __init__(self, n, m, di, i, u, du):
        media.__init__(self, n, di, i, u, du)
        self.Manufacturer = m

    def show(self):
        print (self.name,  self.Manufacturer,  self.IMDB_score, self.url, self.duration, self.casts)

class  Documentary(media) :
    def __init__(self, n, di, dg, i, u):
        media.__init__(self, n, di, i, u)
        self.Documentary_genre = dg

    def show(self):
        print (self.name, self.director,  self.Documentary_genre,  self.IMDB_score, self.url, self.duration, self.casts)

class series(media):
    def __init__(self, n, di, i, s, u, c):
        super().__init__(n, di, i, u, c)
        self.Seasons  = s

    def show(self):
        print (self.name, self.director, self.IMDB_score, self.Episodes, self.Seasons, self.url,  self.casts)

class Film(media):
    def __init__(self, n, di, i, u, du, c):
        super().__init__(n, di, i, u, du, c)

    def show(self):
        print (self.name, self.director, self.IMDB_score, self.url, self.duration, self.casts)

