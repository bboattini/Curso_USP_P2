
a = ['maria', 'josé', 'PAULO', 'Catarina']
b = ['maria', ' josé  ', '  PAULO', 'Catarina  ']
c = ['Bárbara', 'JOSÉ  ', 'Bill']
d = ['oĺá', 'A', 'a', 'casa']
e = ['AAAAAA', 'b']

def primeiro_lex(lista):
    primeiro = lista[-1]
    i = len(lista) - 1
    while i >= 0:
        string = lista[i]
        if (string <= primeiro):
            primeiro = string
        i = i - 1
    return(primeiro)


def clau():
    r1 = primeiro_lex(a)
    r2 = primeiro_lex(b)
    r3 = primeiro_lex(c)
    r4 = primeiro_lex(d)
    r5 = primeiro_lex(e)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
