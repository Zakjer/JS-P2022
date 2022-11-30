rzymskie = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
}
def funkcja(x):
    suma = 0
    for i in range(len(x)):
        if i == len(x)-1:                   
            suma += rzymskie[x[i]]
            return suma
        if rzymskie[x[i]] < rzymskie[x[i+1]]:   
            suma -= rzymskie[x[i]]              
        else:
            suma += rzymskie[x[i]]              
    return suma

        
print(funkcja("MMCM")) 