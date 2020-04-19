plik = open("zad1.txt","w")
for x in range (0,30,1):
   plik.write(str(x*4)+'\n')
plik.close()