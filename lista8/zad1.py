import os 
from datetime import date
plik4 = input("Podaj nazwę pliku, który chcesz otworzyć: ")
zapis = input("Podaj nazwę katalogu, w którym się znajduje: ")
plik = os.path.join(zapis, plik4)
try:
    plik5 = open(plik,"r")
except FileNotFoundError:
    print("Podany plik nie istnieje")
    quit()
tekst = plik5.read()
a = int(input("Podaj przesunięcie szyfru (1-10): "))
if a < 1 or a > 10:
    print("Podałeś niewłaściwą wartość")
def szyfrowanie(x):
    lista = []
    lista2 = []
    for i in x:
        if ord(i) + a >= 65 and ord(i) + a <= 90 or ord(i) + a >= 97 and ord(i) + a <= 122:
            lista.append(ord(i)+a)
        elif ord(i) + a > 90 and ord(i) + a < 101:
            b = 91 - ord(i)
            lista.append(ord(chr(65 + a - b)))
        elif ord(i) + a > 122:
            b = 123 - ord(i)
            lista.append(ord(chr(97 + a - b)))
        else:
            lista.append(ord(i)) 
    for y in lista:
        lista2.append(chr(y))        
    return "".join(lista2)     
plik5.close()
today = date.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)
strKey = str(a) 
b = "plik_zaszyfrowany" + strKey + '_' + str(today.year) + str(today.month) + str(today.day) + ".txt"
try:
    katalog = input("Podaj katalog, w którym chcesz zapisać plik: ")
    plik2 = os.path.join(katalog, b)
    plik3 = open(plik2,"w") 
except FileNotFoundError:   
    print("Taki katalog nie istnieje")
    nowy = input("Podaj nazwę katalogu, który chcesz stworzyć: ")
    os.makedirs(nowy)
    plik2 = os.path.join(nowy, b) 
    plik3 = open(plik2,"w") 
plik3.write(szyfrowanie(tekst))
plik3.close()     
