
a = [1, 2, 3, 4, 5, 6]
b = [0, 45, 2, 67, 87, -65, 100]
c = [1, 1, 1, 0, 0, 2, 1]

def ordena(L):
    fim = len(L)
    for i in range(fim - 1):
        menor = i
        for j in range(i+1, fim):
            if L[j] < L[menor] :
                menor = j
        L[menor], L[i] = L[i], L[menor]

    return L

def clau():
    print(ordena(a))
    print(ordena(b))
    print(ordena(c))
