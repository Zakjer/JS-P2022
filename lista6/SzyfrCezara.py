def szyfrowanie(x):
    import sys
    lista = []
    lista2 = []
    for i in x:
        if ord(i) == 90:
            lista.append(65)
        elif ord(i) == 122:
            lista.append(97)   
        elif ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
            lista.append(ord(i)+1)
        else:
            lista.append(ord(i))    
    for y in lista:
        lista2.append(chr(y))
    return lista2    

def deszyfrowanie(x):
    import sys
    lista = []
    lista2 = []
    for i in x:
        if ord(i) == 65:
            lista.append(90)
        elif ord(i) == 97:
            lista.append(122)   
        elif ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
            lista.append(ord(i)-1)
        else:
            lista.append(ord(i))    
    for y in lista:
        lista2.append(chr(y))
    return lista2    
        
