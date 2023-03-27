m1=[[1,2,3],[4,5,6]]
m2=[[2,3,4],[5,6,7]]
m3=[[1],[2],[3]]
m4=[[1,2,3]]
def sao_multiplicaveis(m1,m2):
    resultado = False
    if(len(m1[0]) == len(m2)):
        resultado = True
    return resultado
