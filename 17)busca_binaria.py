def busca(lista, elemento):

    primeiro = 0
    ultimo = len(lista) - 1
    
    while primeiro <= ultimo:
        m = (primeiro + ultimo)//2
        print(m)
        if lista[m] == elemento:
            return m
        else:
            if lista[m] > elemento:
                ultimo = m - 1
            else:
                primeiro = m + 1

    return False
                
def clau():

    b1 = busca(['a', 'e', 'i'], 'e')
    print(b1)
    b2 = busca([1, 2, 3, 4, 5], 6)
    print(b2)
    b3 = busca([1, 2, 3, 4, 5, 6], 4)
    print(b3)
