from itertools import chain


x = [[2,4,3],[1,5,6],[9],[7,9,0]]
wynik = list(chain.from_iterable(x)) 
print(wynik) 