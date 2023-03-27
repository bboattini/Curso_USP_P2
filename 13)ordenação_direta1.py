
a = [1, 2, 3, 4, 5, 6]
b = [0, 45, 2, 67, 87, -65, 100]
c = [1, 1, 1, 0, 0, 2, 1]

class lista:
    def __init__(self, L):
        self.L = L

def ordenada(L):
    lista1 = L
    lista2 = []
    
    for k in range(len(L)):
        lista2.append(L[k])
    fim = len(lista1)

    for i in range(fim):
        menor = i
        for j in range(i+1, fim):
            if lista2[j] < lista2[i] :
                menor = j
        lista2[menor], lista2[i] = lista2[i], lista2[menor]

    if lista1 == lista2 :
        return(True)
    else :
        return(False)

def clau():
    print(ordenada(a))
    print(ordenada(b))
    print(ordenada(c))
    
