x = str(input("Podaj dowolną liczbę całkowitą z przedziału 1-1999: "))
def funkcja(x):
    a = []
    i = -1
    liczby = {0:"",1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'piec',6:'szesc',7:'siedem',8:'osiem',9:'dziewiec',10:'dziesiec',
11:'jedenascie',12:'dwanascie',13:'trzynascie',14:'cztrenascie',15:'pietnascie',16:'szescnacie',17:'siedemnascie',
18:'osiemnacie',19:'dziewietnascie',20:'dwadziescia',30:'trzydziesci',40:'czterdziesci',50:'piedziesiat',60:'szescdziesiat',
70:'siedemdziesiat',80:'osiemdziesiat',90:'dziewiecdziesiat',100:'sto',200:'dwiescie',300:'trzysta',400:'czterysta',
500:'piecset',600:'szescset',700:'siedemset',800:'osiemset',900:'dziewiecset',1000:'tysiac'}
    while len(x) - 1 > i:
        i += 1
        a.append(int(x[i]))
    if len(a) == 1:
        print(liczby[a[0]]) 
    elif len(a) == 2:
        print(liczby[a[0]*10], liczby[a[1]])    
    elif len(a) == 3:
        print(liczby[a[0]*100], liczby[a[1]*10], liczby[a[2]]) 
    elif len(a) == 4:
        print(liczby[a[0]*1000], liczby[a[1]*100], liczby[a[2]*10], liczby[a[3]]) 

print(funkcja(x)) 


        
