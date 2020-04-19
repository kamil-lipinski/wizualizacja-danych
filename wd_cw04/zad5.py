class ciag:
    def __init__(self,a1,r,n):
        self.a1=int(a1)
        self.r=int(r)
        self.n=int(n)
    
    def wyswietl_dane(self):
        print('a1 = '+str(self.a1))
        print('roznica = '+str(self.r))
        print('dlugosc = '+str(self.n))

    def policz_sume(self):
        ostatni= self.a1 + (self.n - 1)*self.r
        suma= (self.a1 + ostatni)/2*self.n
        print('suma = '+str(suma))


obiekt=ciag(0,3,5)
obiekt.wyswietl_dane()
obiekt.policz_sume()
