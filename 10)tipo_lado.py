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

def clau():
    t = Triangulo(4,4,4)
    y = Triangulo(3,4,5)
    u = Triangulo(3,2,3)
    i = Triangulo(5,5,2)

    return(t.tipo_lado() , y.tipo_lado(), u.tipo_lado(), i.tipo_lado())
