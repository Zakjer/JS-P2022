from SzyfrCezara import szyfrowanie, deszyfrowanie
x = input("Podaj dowolne zdania: ")
print("Te zdania po zaszyfrowaniu to:", szyfrowanie(x))
print("Te zdania po deszyfrowaniu to:",deszyfrowanie(szyfrowanie(x))) 
