
a = [4, 5, 2, 15, -5]
b = [2, 2, 2, 2, 2]
c = [1, 2, 3, 4, 5]
def encontra_impares(lista):
    n = len(lista)
    for i in range(n):
        if (lista[i]%2 == 0):
            lista.remove(lista[i])
            return encontra_impares(lista)
            
    return lista

def clau():
    print(encontra_impares(a))
    print(encontra_impares(b))
    print(encontra_impares(c))
