class robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    
    def idz_w_gore(self,ile_krokow):
        self.y=self.y + ile_krokow * self.krok

    def idz_w_dol(self,ile_krokow):
        self.y=self.y - ile_krokow * self.krok

    def idz_w_lewo(self,ile_krokow):
        self.x=self.x - ile_krokow * self.krok

    def idz_w_prawo(self,ile_krokow):
        self.x=self.x + ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        print('wspolrzedne : ' +str(self.x),',' +str(self.y))

obiekt= robaczek(0,0,1)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_lewo(2)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_prawo(3)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_dol(1)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_gore(5)
obiekt.pokaz_gdzie_jestes()
