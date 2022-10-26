import re
x= input("Podaj haslo różnych znaków: ")
if re.search("[a-z] [A-Z] [0-9] #$@", x) and len(x) > 6 and len(x) < 16:
    print("Twoje hasło jest poprawne")
else:
    print("Twoje hasło nie spełnia wymagań")   

    

