import random

def lista_grande(n):
    lista = []
    for i in range(n):
        r = random.randint(-10*n,10*n)
        lista.append(r)
    return lista

def clau():
    print(lista_grande(10))
    print(lista_grande(4))
    print(lista_grande(67))
