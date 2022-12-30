try:
    plik2 = open("PESEL.txt","r")
except FileNotFoundError:
    print("Podany plik nie istnieje")
    quit()
plik = open("PESEL_dane.txt","w",encoding="utf-8")    
for i in range(1,11):
    odczyt = plik2.readline()
    suma,i = 0,0
    a1 = int(odczyt[0]) * 1
    b1 = str(a1)
    if len(b1) == 2:
        c1 = int(b1[1])
    else:
        c1 = int(odczyt[0]) * 1
    a2 = int(odczyt[1]) * 3
    b2 = str(a2)
    if len(b2) == 2:
        c2 = int(b2[1])
    else:
        c2 = int(odczyt[1]) * 3
    a3 = int(odczyt[2]) * 7
    b3 = str(a3)
    if len(b3) == 2:
        c3 = int(b3[1])
    else:
        c3 = int(odczyt[2]) * 7
    a4 = int(odczyt[3]) * 9
    b4 = str(a4)
    if len(b4) == 2:
        c4 = int(b4[1])
    else:
        c4 = int(odczyt[3]) * 9
    a5 = int(odczyt[4]) * 1
    b5 = str(a5)
    if len(b5) == 2:
        c5 = int(b5[1])
    else:
        c5 = int(odczyt[4]) * 1
    a6 = int(odczyt[5]) * 3
    b6 = str(a6)
    if len(b6) == 2:
        c6 = int(b6[1])
    else:
        c6 = int(odczyt[5]) * 3
    a7 = int(odczyt[6]) * 7
    b7 = str(a7)
    if len(b7) == 2:
        c7 = int(b7[1])
    else:
        c7 = int(odczyt[6]) * 7
    a8 = int(odczyt[7]) * 9
    b8 = str(a8)
    if len(b8) == 2:
        c8 = int(b8[1])
    else:
        c8 = int(odczyt[7]) * 9
    a9 = int(odczyt[8]) * 1
    b9 = str(a9)
    if len(b9) == 2:
        c9 = int(b9[1])
    else:
        c9 = int(odczyt[8]) * 1
    a10 = int(odczyt[9]) * 3
    b10 = str(a10)
    if len(b10) == 2:
        c10 = int(b10[1])
    else:
        c10 = int(odczyt[9]) * 3

    suma = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
    if len(str(suma)) == 2:
        a = str(suma)
        sprawdzenie = 10 - int(a[1])
    else:
        sprawdzenie = 10 - suma    
    if sprawdzenie != int(odczyt[10]): 
        print("PESEL nie jest zdefiniowany poprawnie")
        quit()    
    plik.write("Nr PESEL: "+ odczyt[0]+odczyt[1]+odczyt[2]+odczyt[3]+odczyt[4]+odczyt[5]+odczyt[6]+odczyt[7]+odczyt[8]+odczyt[9]+odczyt[10]+"\t")
    if int(odczyt[2]) == 0 or int(odczyt[2]) == 1:
        plik.write(f"Data urodzenia: 19{odczyt[0]}{odczyt[1]}-{odczyt[2]}{odczyt[3]}-{odczyt[4]}{odczyt[5]}") 
    elif int(odczyt[2]) == 2:
        plik.write(f"Data urodzenia: 20{odczyt[0]}{odczyt[1]}-0{odczyt[3]}-{odczyt[4]}{odczyt[5]}")
    elif int(odczyt[2]) == 3: 
        plik.write(f"Data urodzenia: 20{odczyt[0]}{odczyt[1]}-1{odczyt[3]}-{odczyt[4]}{odczyt[5]}")     
    if int(odczyt[9])%2 == 0:
        plik.write("\tPłeć: kobieta")
    else:
        plik.write("\tPłeć: mężczyzna ")   
    plik.write("\n")     
plik.close()              
plik2.close()



