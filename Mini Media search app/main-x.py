#Video media management
from Film import Film
from Series import Series
from Documentary import Documentary
from Clip import Clip


class Main():
    def __init__(self):

        try:
            f = open('database.csv','r')
        except:
            print('error! database not found')

        big_text = f.read()
        parts = big_text.split('\n') 

        self.medias= []
        i = 0
        
        while i < len(parts):
            info = parts[1].split(',')

            if info[1] == 'Film':
                self.medias.append(Film(info))
            elif info[1] == 'Series':
                self.medias.append(Series(info))
            elif info[1] == 'Documentary' :
                self.medias.append(Documentary(info))
            elif info[1] == 'Clip' :
                self.medias.append(Clip(info)) 
            else :
                print ('wrong data !  "The data must be a Film, Series, Documentary or Clip."')
            
            i += 1
        print('medias:' ,self.medias)
 
        self.show_meun()

    def show_meun(self):
        print (" 1- Show media.\n 2- add media .\n 3-View media profile. \n 4- delete media .\n 5- download media .\n 6- Search media by time.n\ 7- save and exit .")

        user_select = input('Please select your preferred option.')

        if user_select == '1':
            self.Show_media()
        elif user_select == '2':
            self.add_media()
        elif user_select == '3':
            pass 
        elif user_select == '4':
            pass 
        elif user_select == '5':
            pass 
        elif user_select == '6':
            pass 
        elif user_select == '7':
            pass 

        else :
            print ('wrong input !')

    def Show_media(self):
        for p in self.medias:
            p.show()

        self.show_meun()    
    def add_media(self):
        while True:
            Select_item = input("Choose what media you add? \n Clip? \n Documentary? \n Series? \n Film?")

            if Select_item == "Clip":
                id = input('id:')
                What_media = input('Type the Clip. ') 
                name = input('name: ')
                IMDB_score = input('IMDB-score: ')
                director = input('director: ')
                duration= input('duration: ')
                url = input('url: ')

                info = [id, What_media, name, IMDB_score, director, duration, url]

                if What_media == 'Clip':
                    self.medias.append(Clip(info))
                else:
                    print('Wrong data! ')
                self.show_meun()    
            elif Select_item == "Documentary":
                id = input('id:')
                What_media = input('Type the Documentary. ') 
                name = input('name: ')
                IMDB_score = input('IMDB-score: ')
                director = input('director: ')
                duration= input('duration: ')
                url = input('url: ')

                info = [id, What_media, name, IMDB_score, director, duration, url]

                if What_media == 'Documentary':
                    self.medias.append(Documentary(info))
                else:
                    print('Wrong data! ')
                self.show_meun()    
            elif Select_item == "Series":
                id = input('id:')
                What_media = input('Type the Series. ') 
                name = input('name: ')
                IMDB_score = input('IMDB-score: ')
                director = input('director: ')
                duration= input('duration: ')
                casts = input('Three of the casts : ')
                url = input('url: ')
                Seasons = input('Seasons: ')
                info = [id, What_media, name, IMDB_score, director, duration, casts, url, Seasons]

                if What_media == 'Series':
                    self.medias.append(Series(info))
                else:
                    print('Wrong data! ')
                self.show_meun()    
            elif Select_item == "Film":
                id = input('id:')
                What_media = input('Type the Film. ') 
                name = input('name: ')
                IMDB_score = input('IMDB-score: ')
                director = input('director: ')
                duration= input('duration: ')
                casts = input('Three of the casts : ')
                url = input('url: ')

                info = [id, What_media, name, IMDB_score, director, duration, casts, url]

                if What_media == 'Film':
                    self.medias.append(Film(info))
                else:
                    print('Wrong data! ')
                self.show_meun()    
main = Main()