from SzyfrCezara import szyfrowanie, deszyfrowanie
x = input("Podaj dowolne zdania: ")
print("Te zdania po zaszyfrowaniu to: ")
print(szyfrowanie(x))
print("\n", "Te zdania po deszyfrowaniu to: ") 
print(deszyfrowanie(szyfrowanie(x)))
