def insertion_sort(lista1):

    fim = len(lista1) - 1
    lista2 = lista1[:]

    for i in range(fim - 1, 0, -1):
        for j in range(i+1):
            if lista2[j] > lista2[j+1]:
                lista2[j], lista2[j+1] = lista2[j+1] , lista2[j]

    return lista2

a = [1,3,6,3,2,8,5,3,0,7,3,1]
b = [3,3,3,3,3,2,4,4,4,3]
c = [1,0,1]

def clau():
    print(insertion_sort(a))
    print(insertion_sort(b))
    print(insertion_sort(c))
