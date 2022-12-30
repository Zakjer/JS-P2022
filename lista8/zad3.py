def losowy_pesel():
    from random import randint
    a1 = randint(0,9)
    a2 = randint(0,9)
    if (a1 == 0 or a1 == 1) or (a1 == 2 and a2 <= 3):
        rocznik = randint(1,2)
        if rocznik == 1: #rocznik 1900-1999
            a3 = randint(0,1)
            if a3 == 0:
                a4 = randint(1,9)
            elif a3 == 1:
                a4 = randint(0,2)
        elif rocznik == 2: #rocznik 2000-2023
            a3 = randint(2,3)
            if a3 == 2:
                a4 = randint(1,9)
            elif a3 == 3:
                a4 = randint(0,2)
    else:
        a3 = randint(0,1)
        if a3 == 0: 
                a4 = randint(1,9)
        elif a3 == 1:
                a4 = randint(0,2)
    a5 = randint(0,3)
    if a5 == 3:
        a6 = 0
        a6 == randint(0,1)
    elif a5 == 0:
        a6 = randint(1,9)
    elif a5 == 1 or a5 == 2:
        a6 = randint(0,9)
    a7 = randint(0,9)    
    a8 = randint(0,9)    
    a9 = randint(0,9)
    a10 = randint(0,9)    
    #Obliczanie liczby kontrolnej
    b2 = str(a2*3) 
    if len(b2) == 2:
        c2 = int(b2[1])
    else:
        c2 = a2 * 3
    b3 = str(a3*7) 
    if len(b3) == 2:
        c3 = int(b3[1])
    else:
        c3 = a3 * 7
    b4 = str(a4*9) 
    if len(b4) == 2:
        c4 = int(b4[1])
    else:
        c4 = a4 * 9
    b6 = str(a6*3) 
    if len(b6) == 2:
        c6 = int(b6[1])
    else:
        c6 = a6 * 3            
    b7 = str(a7*7) 
    if len(b7) == 2:
        c7 = int(b7[1])
    else:
        c7 = a7 * 7
    b8 = str(a8*9) 
    if len(b8) == 2:
        c8 = int(b8[1])
    else:
        c8 = a8 * 9
    b10 = str(a10*3) 
    if len(b10) == 2:
        c10 = int(b10[1])
    else:
        c10 = a10 * 3          
    test = a1 + c2 + c3 + c4 + a5 + c6 + c7 + c8 + a9 + c10
    if len(str(test)) == 2:
        d = str(test)
        a11 = 10 - int(d[1])    
    else:
        a11 = 10 - test
    if a11 == 10:
        a11 = 0
    lista = str(a1),str(a2),str(a3),str(a4),str(a5),str(a6),str(a7),str(a8),str(a9),str(a10),str(a11)
    lista2 = []
    for i in lista:
        lista2.append(i)
    pesel2 = "".join(lista2)  
    return pesel2  
plik = open("PESEL.txt","w")        
for i in range(1,11):
    plik.write(losowy_pesel())
    plik.write("\n")           
plik.close()





