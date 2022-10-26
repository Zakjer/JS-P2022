from math import sqrt 
print("ax^2 + bx +c")
a = float(input("Podaj dowolną wartość a: "))
b = float(input("Podaj dowolną wartość b: "))
c = float(input("Podaj dowolną wartość c: "))
if a == 0:
    print("Twoje równanie nie jest kwadratowe")
else:
    delta = b ** 2 - (4 * a * c)   
    if delta < 0:
        print("Twoje równanie nie ma pierwiastków rzeczywistych")
    elif delta == 0:
        print("Twoje równanie ma jeden pierwiastek rzeczywisty")
        print("x 1,2 = ", -b / (2 * a))
    else:
        print("Twoje równanie ma dwa pierwiastki rzeczywiste")
        print("x 1 = ", (-b - sqrt(delta)) / (2 * a))
        print("x 2 = ", (-b + sqrt(delta)) / (2 * a))


