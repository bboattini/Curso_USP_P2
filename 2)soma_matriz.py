m1=[[1,2,3],[4,5,6]]
m2=[[2,3,4],[5,6,7]]
m3=[[1],[2],[3]]

def soma_matrizes(m1, m2):
    soma = False
    if(len(m1)==len(m2) and len(m1[0]) == len(m2[0])):
        soma=[]
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                a = m1[i][j] + m2[i][j]
                linha.append(a)
            soma.append(linha)
    return soma
