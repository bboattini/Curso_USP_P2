
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

def clau1():
    print(fatorial(0))
    print(fatorial(1))
    print(fatorial(2))
    print(fatorial(3))
    print(fatorial(4))
    print(fatorial(5))
    print(fatorial(6))
    print(fatorial(7))
    
