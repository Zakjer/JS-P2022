lista=[]
x=1
j=1
z=1
i=int(input("Podaj liczbę: "))
while x<=i:
    lista.clear()
    j=1
    while j <=10:
        if j*x<10:
            lista.append("  "+str(j*x))
        elif j*x>=10 and j*x<100:
            lista.append(" "+str(j*x))
        elif j*x>=100 and j*x<1000:
            lista.append(str(j*x))
        j+=1
    a= "  ".join(lista)
    print(a)
    x += 1
    







