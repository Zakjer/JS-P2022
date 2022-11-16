from math import pi 
def konwertowanie(x):
    if x < 10:
        print("To ", x * (180/pi), " stopnie")
    else:
        print("To", x * (pi/180), " radianów")

konwertowanie(3.14)            