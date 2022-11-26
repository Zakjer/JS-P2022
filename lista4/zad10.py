a = int(input("Podaj dowolną liczbę całkowitą: "))
b = int(input("Podaj liczbę całkowitą mniejszą od poprzedniej: "))
i = -1
while b > i - 1:
    i += 1
    if a%(b-i) == 0 and b%(b-i) == 0:
        print("Największy wspólny dzielnik tych liczb to: ", (b-i))
        break
    else:
        continue      


