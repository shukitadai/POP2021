import datetime
import os
import pickle

class Manga_ka:
    def __init__(self):
        self.name = ""
        self.country = ""
        self.publisher = ""
        self.gender = ""
        self.date_of_birht = \
                    datetime.date.today()
        self.manga_list = []
        self.genre = "\n"
    def __str__(self):
        mangas = "\n"
        for x in self.manga_list:
            mangas += x + "\n"
        return self.name + "\n" +self.publisher \
               + mangas

        
data = Manga_ka()
if os.path.exists("Wakui ken"):
    file = open("Wakui ken","rb")
    data = pickle.load(file)
    file.close()
else:
    file = open("Wakui ken","wb")
    data = Manga_ka()
    data.manga_list.append("Tokyo Revengers")
    data.name = "Wakui ken"
    data.country = "Japan"
    data.publisher = "Magajin"
    data.gender = "Male"
    data.genre = "Syounenn Manga"

    pickle.dump(data,file)
    file.close()

print(data)

