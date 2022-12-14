def szyfrowanie(x):
    klucz= {"a" : "y" ,"e" : "i","i" : "o","o" : "a","y" : "e"}
    lista = []
    for i in x:
        if i in klucz:
            lista.append(klucz[i])
        else:
            lista.append(i)
    return lista                 
             
