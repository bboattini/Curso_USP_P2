class Triangulo():
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return(self.a + self.b + self.c)

    def tipo_lado(self):
        if self.a == self.b and self.b ==self.c :
            return("equilátero")
        if self.a != self.b and self.a != self.c and self.b != self.c :
            return("escaleno")
        else :
            return("isósceles")

    def retangulo(self):
        ret = False
        h = self.a
        c1 = self.b
        c2 = self.c
        if self.tipo_lado() == "escaleno" :
            if h < self.b :
                h, c1 = self.b, h
            if h < self.c :
                h, c2 = self.c, h
            if (h**2 == (c1**2 + c2**2)) :
                ret = True
        
        return(ret)

    def semelhantes(self, T):
        sem = False
        t1 = [self.a, self.b, self.c]
        t2 = [T.a, T.b, T.c]
        if t1[0] >= t2[0]:
            lista = []
            for i in range(len(t1)):
                d = t1[i]%t2[i]
                lista.append(d)
            if lista == [0, 0, 0]:
                    sem = True
        if t1[0] < t2[0]:
            lista = []
            for i in range(len(t1)):
                d = t2[i]%t1[i]
                lista.append(d)
            if lista == [0, 0, 0]:
                    sem = True
        return(sem)
            


def clau():
    t = Triangulo(4,4,4)
    y = Triangulo(3,4,5)
    u = Triangulo(10,10,10)
    i = Triangulo(5,5,5)

    return(t.semelhantes(t), u.semelhantes(i), i.semelhantes(u))
