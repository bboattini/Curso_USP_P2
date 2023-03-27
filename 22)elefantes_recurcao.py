
def incomodam(n):
    if type(n)==int and n > 0:
        return "incomodam " + incomodam(n-1)
    else:
        return ""

def elefantes(n):
    if type(n)==int and n == 1:
        return "Um elefante incomoda muita gente\n"
    if type(n)==int and n == 2:
        return elefantes(n-1) + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
    if type(n)==int and n > 2:
        return elefantes(n-1) + str(n-1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
    else:
        return ""

def clau1():
    print(incomodam(5))
    print(incomodam(3))
    print(incomodam(0))
    print(incomodam(-5))
    print(incomodam(5.5))
def clau2():
    print(elefantes(2))
    print(elefantes(4))
    print(elefantes(-5))
    print(elefantes(5.5))
    
