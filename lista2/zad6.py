lista = ["Kasia", "Basia", "Marek", "Darek"]
lista.append("Józek")
lista.extend(["Ania", "Basia"]) 
lista.sort() 
print(lista[3]) 
print(lista[:2]) 
print(lista[-2:]) 
while "Basia" in lista: 
    lista.remove("Basia") 
print(len(lista)) 
krotka = tuple(lista)
print(krotka) 