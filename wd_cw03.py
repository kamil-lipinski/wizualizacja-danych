from math import *
# zadanie 1
def zadanie_1():
    A = [1/x for x in range (1,11,1)]
    B = [2**i for i in range (11)]
    C = [x for x in B if x % 4 == 0]
    print(A)
    print(B)
    print(C)

# zadanie 2
def zadanie_2():
    import random
    macierz = [[random.randint(0,9) for j in range (0,4,1)] for i in range (0,4,1)]
    przekatna = [macierz[i][j] for i in range (0,4,1) for j in range (0,4,1) if i==j]
    print('Macierz:')
    print(macierz[0])
    print(macierz[1])
    print(macierz[2])
    print(macierz[3])
    print('Przekątna: ',przekatna)

# zadanie 3
def zadanie_3():
    stara_lista = {
        'warzywa': 'kg',
        'czipsy': 'paczka',
        'sok': 'karton',
    }
    nowa_lista = {value: key for key, value in stara_lista.items()}
    print('Oryginalny słownik:')
    print(stara_lista)
    print('Odwrócony słownik:')
    print(nowa_lista)

# zadanie 4
def monotonicznosc(a):
    if (a>0):
        return 'Funkcja rosnaca'
    if (a<0):
        return 'malejaca'
    if(a==0):
        return 'stala'

def zadanie_4():   
    print(monotonicznosc(2))

# zadanie 5
def proste(a1,a2):
    if(a1==a2):
        return 'rownolegle'
    if(a1*a2==-1):
        return 'prostopadle'
    else:
        return 'nie sa ani rownolegle ani prostopadle'

def zadanie_5():   
    a1 = input('Podaj a1: ')
    b1 = input('Podaj b1: ')
    a2 = input('Podaj a2: ')
    b2 = input('Podaj b2: ')
    print('Proste y1 i y2 sa ',proste(float(a1), float(a2)))

# zadanie 6
def okrag(a=0, b=0, x=0, y=0):
    return ((x-a)**2 + (y-b)**2)**0.5

def zadanie_6():
    a = input('Podaj współrzędną a: ')
    b = input('Podaj współrzędną b: ')
    x = input('Podaj współrzędną x: ')
    y = input('Podaj współrzędną y: ')
    print('Promień okręgu wynosi:',okrag(float(a), float(b), float(x), float(y)))

# zadanie 7
def pitagoras(a=0, b=0):
    return (a**2 + b**2)** 0.5

def zadanie_7():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    print('Przeciwprostokatna ma dlugosc ',pitagoras(a,b))
    
# zadanie 8
def suma_ciagu(a1=1, r=1, ile=10):
    return ile*((2*a1) + (ile-1)*r)/2

def zadanie_8():
    a1 = float(input('Podaj a1: '))
    r = float(input('Podaj r: '))
    ile = int(input('Podaj ile: '))
    print('suma = ',str(suma_ciagu(a1, r, ile)))

# zadanie 9
def iloczyn_ciagu(* liczby):
    if(len(liczby) == 0):
        return 0
    else:
        iloczyn = 1
        for i in liczby:
            iloczyn = iloczyn * i
        return iloczyn

def zadanie_9():
    print('iloczyn dla ciągu 1,2,3,4:', iloczyn_ciagu(1,2,3,4))
    print('iloczyn dla ciągu 1,2,0,4:', iloczyn_ciagu(1,2,0,4))

# zadanie 10
 def ilosc_produnktow(**lista_zakupow):
    suma = 0.0
    for i in lista_zakupow:
        suma = suma + float(lista_zakupow[i])
    return suma

def zadanie_10():
    print('liczba wszystkich produktów:', ilosc_produnktow(sok=3,jablko=5,
          baton=6, woda=3, olowek=1, banan=7))







zadanie_10()