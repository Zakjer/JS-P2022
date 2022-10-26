import cmath 
x = complex(input("Podaj dowolną liczbę zespoloną: ")) 
zmod = abs(x) 
zarg = cmath.phase(x) 
zc = x.conjugate() 
print(zc) 
print(zmod)
print(zarg)