# zadanie 1
def zadanie_1():
    int_1 = 1
    int_2 = 2
    float_1 = 1.22 
    float_2 = -4.5646
    complex_1 = 5 + 2j
    complex_2 = 9 - 3j
    string_1 = 'wyraz'
    string_2 = 'aaaaaaaaaa'
    print('int: ', int_1, int_2)
    print('float: ', float_1, float_2)
    print('complex: ', complex_1, complex_2)
    print('string: ', string_1, string_2)

# zadanie 2
def zadanie_2():
    a=1
    b=5
    print('dodawanie:', a, '+', b, '=', a+b)
    print('odejmowanie:', a, '-', b, '=', a-b)
    print('mnożenie:', a, '*', b, '=', a*b)
    print('dzielenie:', a, '/', b, '=', a/b)
    print('dzielenie calkowite:', a, '//', b, '=', a//b)
    print('reszta z dzielenia:', a, '%', b, '=', a%b)
    print('potegowanie:', a, 'do potegi', b, '=', a**b)
    print('potegowanie:', a, 'do potegi', b, '=', pow(a,b))

# zadanie 3
def zadanie_3():
    print('a = 5')
    a = 2
    a += 1
    print('a += 7:', a)
    a = 2
    a -= 1
    print('a -= 7:', a)
    a = 2
    a *= 1
    print('a *= 7:', a)
    a = 2
    a /= 1
    print('a /= 7:', a)
    a = 2
    a **= 1
    print('a **= 7:', a)
    a = 2
    a %= 1
    print('a %= 7:', a)

# zadanie 4
def zadanie_4():
    print('a do 2 = ', pow(a, 2))
    print('(ln(5+sin^2(8)))^(1/6) = ', pow( log(5 + pow(sin(8), 2)), 1/6))
    print('⌊1,77⌋ = ', floor(1.77))
    print('⌈3,82⌉ = ', ceil(3.82))

# zadanie 5
def zadanie_5():
    imie = 'Kamil'
    nazwisko = 'Lipiński'
    print(str.capitalize(imie), str.capitalize(nazwisko))

# zadanie 6
def zadanie_6():
    piosenka = 'la la la la la'
    print('la powtarza sie', piosenka.count('la'), 'razy')

# zadanie 7
def zadanie_7():
    napis = 'przyklad'
    print('napis =', napis)
    print('Druga litera =', napis[1])
    print('ostatnia litera =', napis[-1])

# zadanie 8
def zadanie_8():
    piosenka = 'la la la la la la la'
    print(str.split(piosenka))

# zadanie 9
def zadanie_9():
    z_string = 'tekst'
    z_float = 243
    z_hexdec = hex(255)
    print('string: %(zm)s' % {'zm': z_string})
    print('float: %(zm)f' % {'zm': z_float})
    print('szestnastkowe: %(zm)s' % {'zm': z_hexdec})

# zadanie 10
def zadanie_10():
    filmy = ['Film2',
             'Film3', 'Film4',
             'Film5', 'Film1']
    print('Lista filmów przed posortowaniem:\n', filmy)
    filmy.sort()
    print('Lista filmów po posortowaniu:\n', filmy)

# zadanie 11
def zadanie_11():
    tabelka = [['kat', '0', '30', '45', '60', '90'],
               ['sin', sin(0), sin(30), sin(45), sin(60), sin(90)],
               ['cos', cos(0), cos(30), cos(45), cos(60), cos(90)],
               ['tan', tan(0), tan(30), tan(45), tan(60), tan(90)]]
    print(tabelka[0])
    print(tabelka[1])
    print(tabelka[2])
    print(tabelka[3])

# zadanie 12
def zadanie_12():
    napis = 'dowolnie dlugie zdanie'
    lista_slow = str.split(napis)
    print(napis)
    print(lista_slow)

# zadanie 13
def zadanie_13():
    znajomi = {
        'Gruby': ['Czarek', 'Szymański'],
        'Łysy': ['Jan', 'Kowalski'],
        'Chudy': ['Juliusz', 'Nowak'],
        'Duży': ['Ferdynand', 'Lewandowski'],
        'Młody': ['Karol', 'Jankowski'],
        'Stary': ['Marcin', 'Dąb'],
        'Krótki': ['Adam', 'Łoś'],
        'Seba': ['Sebastian', 'Kowalczyk'],
        'Skoczek': ['Adam', 'Małysz'],
        'Ostatni': ['Robert', 'Kubica'],
    }
    print(znajomi['Gruby'])
    print(znajomi['Ostatni'])

# zadanie 14
def zadanie_14():
    slownik = {
        'xDDDDDDDDDDDDDDD': ['xD'],
        'cb': ['Ciebie'],
        'nvm': ['Nie ważne'],
        'nwm': ['Nie Wiem'],
    }

# zadanie 15
def zadanie16():
    liczby = {
        'I': ['1'],
        'v': ['5'],
        'X': ['10'],
        'L': ['50'],
        'C': ['100'],
        'D': ['500'],
        'M': ['1000'],
    }

# zadanie 16
def zadanie16():
    gry = {
        'CS': ['Counters Strike : Global Offensive],
        'FIFA': ['FIFA20'],
        'GTA5': ['Grand Theft Auto V'],
    }