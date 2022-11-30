import sys
lista = []
napis = "Adam Nowak i Michał Kowalski oraz Kacper Kowal pojechali na ryby"
i = -1
while i < len(napis) - 1:
    i += 1
    if napis[i] == "N" and napis[i+1] == "o" and napis [i+2] == "w" and napis[i+3] == "a" and napis[i+4] == "k":
        lista.append("N.")
        i += 4
    elif napis[i] == "K" and napis[i+1] == "o" and napis [i+2] == "w" and napis[i+3] == "a" and napis[i+4] == "l" and napis[i+5] == "s" and napis[i+6] == "k" and napis[i+7] == "i":
        lista.append("K.")
        i += 7
    elif napis[i] == "K" and napis[i+1] == "o" and napis [i+2] == "w" and napis[i+3] == "a" and napis[i+4] == "l":
        lista.append("K.")
        i += 4        
    else:
        lista.append(napis[i])     

for y in lista:
    sys.stdout.write(y)        


