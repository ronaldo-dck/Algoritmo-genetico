import math


def decode(gene):
    """decodifica um gene para float"""
    a = 0
    for i, g in enumerate(gene):
        a += g*2**(-(i))
    return a

def limiar(gene):
    """garante que todos os genes estão no intervalo [0, 0,5["""
    gene[0] = 0
    gene[1] = 0

def calc(x, y):
    """calcula o fitness dos indivíduos"""
    return x * math.sin(4 * math.pi * x) - y * math.sin(4 * math.pi * y + math.pi) + 1
