def funkcja(list):
    for x in lista:
        for y in lista:
            if x == y:
                lista.remove(y) 
lista = []
b = 0
a = int(input("Ile elemntów ma mieć lista?:"))  
while b < a: 
    b += 1
    c = input(f"Podaj {b} element listy: ")
    lista.append(c)
funkcja(lista) 
print(lista) 









    

   
