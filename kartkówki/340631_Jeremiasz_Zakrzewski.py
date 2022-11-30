def funkcja(s):
    import sys
    lista = []
    for x in s:
        if x == "A":
            lista.append("T")
        elif x == "C":
            lista.append("G")
        elif x == "T":
            lista.append("A")
        elif x == "G":
            lista.append("C")
        else:
            print("Zła sekwencja")
            lista = []
    for i in reversed(lista):
        sys.stdout.write(i)
        
