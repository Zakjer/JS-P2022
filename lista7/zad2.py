from random import randint
import time 
def losowanie(a):
    lista1 = []
    for i in range(1,a):
        x = randint(1,20)
        lista1.append(x)
    return lista1

def sortowanie(lista):
    i = 1
    while i < len(lista):
        klucz = lista[i] 
        j = i - 1
        while j >= 0 and klucz < lista[j]:
            lista[j + 1] = lista[j] 
            j -= 1
        lista[j + 1] = klucz
        i += 1    
    return lista   

czas1 = time.time()
sortowanie(losowanie(100))
print(time.time() - czas1, end = "\n")
czas1 = time.time()
sortowanie(losowanie(200))
print(time.time() - czas1, end = "\n")
czas1 = time.time()
sortowanie(losowanie(300))
print(time.time() - czas1, end = "\n")