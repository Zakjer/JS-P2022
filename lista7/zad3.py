from zad2 import losowanie
import time
def sortowanie2(lista):
    i = 0
    while i < len(lista) - 1:
        j = 0
        while j < len(lista) - 1:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j + 1], lista[j]
            j += 1    
        i += 1   
    return lista      

czas1 = time.time()
sortowanie2(losowanie(100))
print(time.time() - czas1, end = "\n")
czas1 = time.time()
sortowanie2(losowanie(200))
print(time.time() - czas1, end = "\n")
czas1 = time.time()
sortowanie2(losowanie(300))
print(time.time() - czas1, end = "\n")

        
    