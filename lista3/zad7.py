N = int(input("Wprowadź zakres liczb fibonaciego: "))
wyraz = [0,1]
wynik = 0
print(0,"wyraz Fibonacciego =", 0)
print(1,"wyraz Fibonacciego =", 1)
for j in range(1,N):
    wynik = wyraz[0]+wyraz[1]
    wyraz[0] = wyraz[1]
    wyraz[1] = wynik
    print(j+1,"wyraz Fibonacciego =", wynik)

    


    