# x = int(input("Podaj dowolną liczbę całkowitą: "))
# if x % 2 == 0:
#     print("Podałeś liczbę parzystą")
# else:
#     print("Podałeś liczbę nieparzystą")     

# Program bez "if"
x = int(input("Podaj dowolną liczbę całkowitą: ")) 
print("Liczba", (x%2 and "jest nieparzysta") or "jest parzysta") 
