lista=[]
x=1
z=1
n=int(input("Podaj liczbę kolumn:" ))
m=int(input("Podaj liczbę wierszy: "))
while x<=m:
    lista.clear()
    j=1
    while j <=n:
        if j*x<10:
            lista.append("  "+str(j*x))
        elif j*x>=10 and j*x<100:
            lista.append(" "+str(j*x))
        elif j*x>=100 and j*x<1000:
            lista.append(str(j*x))
        j+=1
    a= "  ".join(lista)
    print(a)
    x+=1