import math

def indDecode(ind):
    """Decodifica os genes binários de um indivíduo para float"""
    x = 0
    y = 0
    for i, g in enumerate(ind['Xbin']):
        x += g*2**(-(i))
    ind['Xdec'] = x
    for i, g in enumerate(ind['Ybin']):
        y += g*2**(-(i))
    ind['Ydec'] = y

def indLimits(ind):
    """Garante que todos os genes de um indivíduo estão dentro do intervalo [0, 0.5["""
    ind['Xbin'][0] = 0
    ind['Xbin'][1] = 0
    ind['Ybin'][0] = 0
    ind['Ybin'][1] = 0

def calc(x, y):
    """Calcula o fitness dos indivíduos"""
    return x * math.sin(4 * math.pi * x) - y * math.sin(4 * math.pi * y + math.pi) + 1
