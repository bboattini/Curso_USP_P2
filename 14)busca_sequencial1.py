
a = ['a', 'e', 'i']
b = [12, 13, 14]
c = ['cabeça', 'bocão', 'Tati', 'Pimentinha']

def busca(L, coisa):
    for i in range(len(L)):
        if L[i] == coisa:
            return i
    return False

def clau():
    print(busca(a, 'e'))
    print(busca(b, 15))
    print(busca(c, 'Pimentinha'))
    print(busca(a, 'Mel'))
    print()
    print()
    print()
    print()


