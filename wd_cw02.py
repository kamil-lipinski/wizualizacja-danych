# zadanie 1
def zadanie_1():
    a = input ('Podaj tekst: ')
    print('Spacja wystepuje', a.count(' '), 'razy')

# zadanie 2
def zadanie_2():
    import sys
    print('Podaj pierwsza liczbe: ')
    a = sys.stdin.readline()
    a = int(a)
    print('Podaj druga liczbe: ')
    b = sys.stdin.readline()
    b = int(b)
    c = a*b
    print('Wynikiem mnozenia tych liczb jest:',c)
    # c = str(c)
    # sys.stdout.write(c)

# zadanie 4
def zadanie_4():
    a = input ('Podaj liczbe: ')
    a = int(a)
    if a<0:
        a = a*-1
        print('Wartoscc bezwzgleda tej liczby to: ',a)
    else:
        print('Wartoscc bezwzgleda tej liczby to: ',a)

# zadanie 5
def zadanie_5():
    a = input ('Podaj liczbe a: ')
    b = input ('Podaj liczbe b: ')
    c = input ('Podaj liczbe c: ')
    a = int(a)
    b = int(b)
    c = int(c)
    if (a>=0 and a<=10) and (a>b or b>c):
        print('Warunki spelnione\n')
    else:
        print('Warunki nie zostaly spelnione')

# zadanie 6
def zadanie_6():
    lista = [5,3,7,20,25,6,15]
    lista.sort()
    for x in lista:
        if(x % 5 == 0):
            print(str(x))

# zadanie 7
def zadanie_7():
    lista = []
    for licznik in range(1, 6, 1):
        liczba = input('podaj '+str(licznik)+' liczbe: ')
        lista.append(int(liczba))
    for licznik in range(0, 5, 1):
        print(str(lista[licznik])+'^2 = '+str(lista[licznik]**2))

# zadanie 8
def zadanie_8():
    lista = []
    i = 0
    while (i<5):
        liczba = input('podaj liczbe: ')
        lista.append(int(liczba))
        i=i+1
    lista.sort()
    print(lista)

# zadanie 9
def zadanie_9():
    a = input('Podaj liczbe: ')
    a = int(a)







