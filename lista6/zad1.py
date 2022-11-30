from trojkat import obwód, pole, boki, kąty
a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
c = float(input("Podaj długość trzeciego boku trójkąta: "))
if a + b < c or a + c < b or b + c < a or a <= 0 or b <= 0 or c <= 0:
    print("Podana figura nie jest trójkątem")
else:
    print("Obwód tego trójkąta wynosi:",obwód(a,b,c), "\n", "Pole tego trójkąta wynosi: ", pole(a,b,c), "\n", boki(a,b,c), "\n" ,kąty(a,b,c))    
