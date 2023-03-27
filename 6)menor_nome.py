
a = ['maria', 'josé', 'PAULO', 'Catarina']
b = ['maria', ' josé  ', '  PAULO', 'Catarina  ']
c = ['Bárbara', 'JOSÉ  ', 'Bill']


def menor_nome(nomes):
    menor = nomes[-1]
    i = len(nomes) - 1
    while i >= 0:
        nome = nomes[i].strip().capitalize()
        if (len(nome) <= len(menor)):
            menor = nome
        i = i - 1
    return(menor)


def clau():
    r1 = menor_nome(a)
    r2 = menor_nome(b)
    r3 = menor_nome(c)
    print(r1)
    print(r2)
    print(r3)
