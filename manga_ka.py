import datetime

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

        

ken_wakui = Manga_ka()
ken_wakui.manga_list.append("Tokyo Revengers")
ken_wakui.name = "Wakui ken"
ken_wakui.country = "Japan"
ken_wakui.publisher = "Magajin"
ken_wakui.gender = "Male"
ken_wakui.genre = "Syounenn Manga"

print(ken_wakui)
