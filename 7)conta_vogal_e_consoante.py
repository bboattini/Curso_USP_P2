
a = 'programamos em python'
b = 'programamos em python' #vogal
c = 'programamos em python' #consoantes

def conta_letras(frase, contar = "vogais"):
########
    if (contar == "consoantes"):
        num = 0
        for i in range(len(frase)):
            if (frase[i] != " " and frase[i] != "A" and frase[i] != "E" and frase[i] != "I" and frase[i] != "O" and frase[i] != "U" and frase[i] != "a" and frase[i] != "e" and frase[i] != "i" and frase[i] != "o" and frase[i] != "u"):
                num = num + 1
########
    else :
        num = 0
        for i in range(len(frase)):
            if (frase[i] == "A" or frase[i] == "E" or frase[i] == "I" or frase[i] == "O" or frase[i] == "U" or frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u"):
                num = num + 1

    return(num)
