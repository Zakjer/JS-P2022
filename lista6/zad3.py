def countandSay(n):
    lista = []
    if (n == 1):
        return "1"
    if (n == 2):
        return "1, 11"
    s = "11"
    lista.append("1")
    lista.append("11")
    for i in range(3, n + 1):
        s += '$'
        l = len(s)
        cnt = 1 
        tmp = "" 
        for j in range(1 , l):
            if (s[j] != s[j - 1]):
                tmp += str(cnt + 0)
                tmp += s[j - 1]
                cnt = 1
            else:
                cnt += 1
        s = tmp
        lista.append(s)
    return lista
N = int(input("Ile wyrazów ciągu count and say wypisać?: "))
print(countandSay(N))
