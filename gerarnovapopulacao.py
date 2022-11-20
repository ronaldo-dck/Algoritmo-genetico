import random
import hiperparametros as hp
import decodeecontrole as dc

def seleciona(Populacao):
    """seleciona individuos da população aleatoriamente e devolve o melhor"""

    Selecao = list()

    inds = list()
    i = 0

    if len(Populacao) > 5:
        while i < 5:
            num = random.randint(0, len(Populacao)-1)
            if not (num in inds):
                inds.append(num)
                i += 1
                Selecao.append(Populacao[num])
    else:
        Selecao = Populacao[:]

    Selecao = sorted(Selecao, key=lambda i: i['fitness'], reverse=True)
    return Selecao[0]


def elitismo(Populacao, NewPOP, MelhoresInd):
    """Escolhe o melhor individou e passa para a próxima geração"""
    Populacao = sorted(Populacao, key=lambda i: i['fitness'], reverse=True)
    NewPOP.append(Populacao[0])
    MelhoresInd.append(Populacao[0])
    return NewPOP, MelhoresInd


def mutacao(gene):
    """Muta, com uma chance de 50%, os bits para o valor oposto"""
    for i, b in enumerate(gene):
        if random.random() > hp.TAXA_MUTACAO:
            gene[i] = abs(gene[i]-1)

    return gene


def cruzamento(pai1, pai2):
    """Dados dois pais, realiza o cruzamento com o método de dois pontos aleatórios"""
    pontos = [random.randint(0, 16), random.randint(0, 16)]
    pontos = sorted(pontos)

    filho1 = {}
    filho2 = {}

    aux = pai1['Xbin'][:pontos[0]] + \
        pai2['Xbin'][pontos[0]:pontos[1]] + pai1['Xbin'][pontos[1]:]
    filho1['Xbin'] = mutacao(aux)
    aux = pai2['Xbin'][:pontos[0]] + \
        pai1['Xbin'][pontos[0]:pontos[1]] + pai2['Xbin'][pontos[1]:]
    filho2['Xbin'] = mutacao(aux)
    aux = pai1['Ybin'][:pontos[0]] + \
        pai2['Ybin'][pontos[0]:pontos[1]] + pai1['Ybin'][pontos[1]:]
    filho1['Ybin'] = mutacao(aux)
    aux = pai2['Ybin'][:pontos[0]] + \
        pai1['Ybin'][pontos[0]:pontos[1]] + pai2['Ybin'][pontos[1]:]
    filho2['Ybin'] = mutacao(aux)

    dc.limiar(filho1['Xbin'])
    dc.limiar(filho1['Ybin'])
    dc.limiar(filho2['Xbin'])
    dc.limiar(filho2['Ybin'])

    filho1['Xdec'] = dc.decode(filho1['Xbin'])
    filho1['Ydec'] = dc.decode(filho1['Ybin'])
    filho1['fitness'] = dc.calc(filho1['Xdec'], filho1['Ydec'])

    filho2['Xdec'] = dc.decode(filho2['Xbin'])
    filho2['Ydec'] = dc.decode(filho2['Ybin'])
    filho2['fitness'] = dc.calc(filho2['Xdec'], filho2['Ydec'])

    return filho1, filho2


def novaPop(NewPOP, nElementos, Populacao, MelhoresInd):
    NewPOP.clear()
    elitismo(Populacao, NewPOP, MelhoresInd)
  
    while len(NewPOP) < nElementos:
        p1 = seleciona(Populacao)
        p2 = seleciona(Populacao)
        while p1 == p2:
            p2 = seleciona(Populacao)

        if random.random() < hp.TAXA_CRUZAMENTO:
            filho1, filho2 = cruzamento(p1, p2)
        else:
            filho1 = p1
            filho2 = p2
        NewPOP.append(filho1)
        if len(NewPOP) == nElementos:
            break
        else:
            NewPOP.append(filho2)

    return NewPOP