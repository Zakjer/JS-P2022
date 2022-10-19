import math 
a = float(input("Podaj długość boku trójkąta: ")) 
b = float(input("Podaj długość boku trójkąta: "))
c = float(input("Podaj wartość kąta między tymi bokami: "))
print("Pole trójkąta wynosi:", (1/2 * a * b * math.sin(c * math.pi/180)))