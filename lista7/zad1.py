#Ciąg poprzez iteracje 
N = int(input("Ile wyrazow ciągu Fibonacciego chcesz wyznaczyć: "))
def rekurencyjnie(N):
    wyraz = [0,1]
    suma = 0
    print("1 wyraz ciągu Fibonacciego to: 0")
    for x in range(1,N):
        wyraz[0] = wyraz[1]
        wyraz[1] = suma
        suma = wyraz[0] + wyraz[1]
        print(x+1, "wyraz ciągu Fibonacciego to:", suma)    
     
rekurencyjnie(N)



    