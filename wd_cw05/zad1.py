class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc

    def wyswietl_nazwe(self):
        print('nazwa: ',self.rodzaj)

class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo

    def wyswietl_dane(self):
        print('rozmiar: ',self.rozmiar)
        print('kolor: ',self.kolor)
        print('dla: ',self.dla_kogo)

class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra

    def wyswietl_dane(self):
        print('rodzaj swetra: ',self.rodzaj_swetra)

poliester=Material('poliester',5,5)
koszulka=Ubrania('M','bialy','Jan')
pulower=Sweter('pulower')

poliester.wyswietl_nazwe()
koszulka.wyswietl_dane()
pulower.wyswietl_dane()
