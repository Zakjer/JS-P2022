tablica1 = [1]
tablica2 = [1,1]
n = int(input("Ile chcesz wypisać wierszy? "))
i = 0
while i < n:
    print(" "*(n-i), end="") 
    for k in range(0,len(tablica1)):
        print(tablica1[k], end=" ")
    print("")
    tablica1 = tablica2
    tablica2 = [1]
    j=0
    while j < len(tablica1)-1:
        tablica2.append(tablica1[j]+tablica1[j+1])
        j+=1
    tablica2.append(1)
    i+=1

