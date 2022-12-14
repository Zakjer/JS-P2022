def obwód(a,b,c):
    return(a+b+c)

def pole(a,b,c):
    from math import sqrt
    p = (a+b+c)/2
    return(sqrt(p*(p-a)*(p-b)*(p-c)))

def boki(a,b,c):
    if a == b and b == c:
        return("Trójkąt jest równoboczny")
    elif a == b or a == c or b == c:
        return("Trójkąt jest równoramienny")
    else:
        return("Trójkąt jest różnoboczny")
    
def kąty(a,b,c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return("Trójkąt jest prostokątny")
    elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
        return("Trójkat jest ostrokątny")
    else:
        return("Trójkąt jest rozwartokątny")
        