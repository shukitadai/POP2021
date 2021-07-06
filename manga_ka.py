class Manga_ka:
    def __init__(self):
        self.name = ""
        self.country = ""
        self.publisher = ""
        self.gender = ""
        self.date_of_birht = \
                    datetime.date.today()
        self.manga_list = []
        self.genre = ""

        

ken_wakui = Manga_ka()
ken_wakui.manga_list.append("Tokyo Revengers")
ken_wakui.name = "Wakui  ken"
ken_wakui.country = "Japan"
ken_wakui.publisher = "Magajin"
ken_wakui.gender = ""
print(oda_eichiro.manga_list)
