x = []
y = []
a = -3
b = -2
c = -1
for z in range(100, 401):
    x.append(str(z)) 
for i in x: 
    y.append(int(i[0]))
    y.append(int(i[1]))
    y.append(int(i[2]))   
                 
while c < 900:
    a = a + 3
    b = b + 3
    c = c + 3
    if y[a] %2 == 0 and y[b] %2 == 0 and y[c] %2 == 0:
        print(y[a], y[b], y[c])
    else:
        continue    



