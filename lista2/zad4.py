import sys
lista = []
x = input("Podaj dowolny napis: ")
i = -1
while i < len(x) - 1:
    i += 1 
    if i == 0:
        lista.append(x[0]) 
    elif x[i] == x[0]:
        lista.append("$")
    else:
        lista.append(x[i]) 

for y in lista:
    sys.stdout.write(y)

# Funkcja sys.stdout.write() powoduje, że kolejne elementy listy są wypisywane w jednej lini.     



