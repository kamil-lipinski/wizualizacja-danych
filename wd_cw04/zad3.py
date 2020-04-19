with open("zad3.txt", "w+") as plik:
    plik.write(str(print("witaj")))
    plik.write(str(print("hej")))

with open("zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")