
a = "AhjkfgD"
b = "gfusfkdghy"
c = "AuhfhGnhbjhbZ"

def maiusculas(frase):
    letras = ""
    for i in range(len(frase)):
        aux = ord(frase[i])
        if (91 > aux and aux > 64):
            letras = letras + frase[i]
    return(letras)
