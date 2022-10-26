x = input("Podaj dowolną literę aflabetu: ")
if len(x) == 1:
    if x in ("aąeęiouy"):
        print("To jest samogłoska")
    else:
        print("To jest spółgłoska")   
else:
    print("Nie podałeś jednej litery")           