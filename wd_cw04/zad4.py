class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=str(nazwa_produktu)
        self.ilosc=int(ilosc)
        self.jednostka_miary=str(jednostka_miary)
        self.cena_jed=float(cena_jed)

    def wyswietl_produkt(self):
        print('nazwa : ' +str(self.nazwa_produktu))
        print('ilosc : ' +str(self.ilosc))
        print('jednostka : ' +str(self.jednostka_miary))
        print('cena za ' +str(self.jednostka_miary), ': ' +str(self.cena_jed))

    def ile_produktu(self):
        return str(self.ilosc)+' '+str(self.jednostka_miary)

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

obiekt = NaZakupy('ziemniaki',3,'kg',2.50)
obiekt.wyswietl_produkt()
print('ile produktu: '+obiekt.ile_produktu())
print('ile w sumie kosztuje produkt: '+str(obiekt.ile_kosztuje())+' zł')