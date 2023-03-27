m1=[[1,2,3],[4,5,6]]
m2=[[2,3,4],[5,6,7]]
m3=[[1],[2],[3]]

def imprime_matriz(m):
        for i in range(len(m)):
            for j in range(len(m[0])):
                if (j == 0):
                        print(str(m[i][j]),end="")
                        k = len(m[0]) - 1
                        if(j == k):
                                print()
                if (j > 0):
                        print(" " + str(m[i][j]),end="")
                        k = len(m[0]) - 1
                        if(j == k):
                                print()
