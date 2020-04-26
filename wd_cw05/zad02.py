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
    
    def __add__(self, other):
        return self.x + other.x

a=Kwadrat(10)
b=Kwadrat(20)
c=Kwadrat(a+b)

print('kwadrat a ma wymiary:', a.x,'na', a.y)
print('kwadrat b ma wymiary:', b.x,'na', b.y)
print('kwadrat c ma wymiary:', c.x,'na', c.y)
