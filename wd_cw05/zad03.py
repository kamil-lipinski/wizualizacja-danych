class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __ge__(self,other):
        if(self.x >= other.x):
            return True
        else:
            return False

    def __gt__(self,other):
        if(self.x > other.x):
            return True
        else:
            return False

    def __le__(self,other):
        if(self.x <= other.x):
            return True
        else:
            return False

    def __lt__(self,other):
        if(self.x < other.x):
            return True
        else:
            return False

a=Kwadrat(10)
b=Kwadrat(20)
print('dlugosc boku kwadratu a: '+str(a.x))
print('dlugosc boku kwadratu b: '+str(b.x))
print('--------')
print('__ge__')
print('kwadrat a >= kwadrat b -',a >= b)
print('kwadrat b >= kwadrat a -',b >= a)
print('--------')
print('__gt__')
print('kwadrat a > kwadrat b -',a >= b)
print('kwadrat b > kwadrat a -',b >= a)
print('--------')
print('__le__')
print('kwadrat a <= kwadrat b -',a >= b)
print('kwadrat b <= kwadrat a -',b >= a)
print('--------')
print('__lt__')
print('kwadrat a < kwadrat b -',a >= b)
print('kwadrat b < kwadrat a -',b >= a)
