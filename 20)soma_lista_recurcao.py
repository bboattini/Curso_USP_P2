
a = [1, 2, 3, 4, 5]
b = [2, 2, 2, 2, 2]
c = [4, 5, 2, 15, -5]

def soma_lista(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    else:
        lista[0] = lista[0] + lista[n - 1]
        return soma_lista(lista[:n - 1])

def clau():
    print(soma_lista(a))
    print(soma_lista(b))
    print(soma_lista(c))
