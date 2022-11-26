from math import pi 
def konwertowanie(x,y):
    if y == "1":
        print("To ", x * (180/pi), " stopni")
    elif y == "0":
        print("To", x * (pi/180), " radianów")
    
x = float(input("Podaj wartość, którą chcesz przekonwertować: "))
y = input("Jeżeli chcesz konwertować stopnie na radiany to wpisz 0, jeżeli chcesz konwertować radiany na stopnie to wpisz 1: ")
konwertowanie(x,y) 