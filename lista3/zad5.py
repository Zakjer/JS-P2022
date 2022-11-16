hasło = list(input("Podaj hasło od 6 do 16 znaków: "))
licznikA=0  #duze litery
licznikB=0  #male litery
licznikC=0  #liczba
licznikD=0  #znak specjalny
for x in hasło:
    if (ord(x) >= 65) & (ord(x) <= 90):      
        licznikA+=1
    if (ord(x) >= 97) & (ord(x) <= 122):
        licznikB+=1
    if x.isnumeric():                        
        licznikC+=1
    if (x=="$") | (x=="#") | (x=="@"):
        licznikD+=1
if(licznikA>0) & (licznikB>0) & (licznikC>0) & (licznikD>0):
    print("Podane hasło spełnia wymagania")
else:
    print("Podane hasło nie spełnia wymagań")

