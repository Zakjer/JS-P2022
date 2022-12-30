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
a = int(plik4[17])
def deszyfrowanie(x):
    lista = []
    lista2 = []
    for i in x:
        if ord(i) - a >= 65 and ord(i) - a <= 90 or ord(i) - a >= 97 and ord(i) - a <= 122:
            lista.append(ord(i)-a)
        elif ord(i) - a < 65 and ord(i) - a > 54:
            b = ord(i) - 64
            lista.append(ord(chr(90 - a + b)))
        elif ord(i) - a < 97 and ord(i) - a > 86:
            b = ord(i) - 96
            lista.append(ord(chr(122 - a + b)))
        else:
            lista.append(ord(i)) 
    for y in lista:
        lista2.append(chr(y))        
    return "".join(lista2)
tekst = plik5.read()
today = date.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)
strKey = str(a) 
b = "plik_deszyfrowany" + strKey + '_' + str(today.year) + str(today.month) + str(today.day) + ".txt"
plik2 = open(b,"w")
plik2.write(deszyfrowanie(tekst))
plik2.close()
plik5.close()     
