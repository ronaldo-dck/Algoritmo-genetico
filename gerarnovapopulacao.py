import random
import hiperparametros as hp
import decodeecontrole as dc

def seleciona(Populacao):
    """Seleciona individuos da população aleatoriamente e devolve o melhor"""
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

    #Ordena a seleção dos melhores para os piores
    Selecao = sorted(Selecao, key=lambda i: i['fitness'], reverse=True)
    return Selecao[0]


def elitismo(Populacao, NewPOP, MelhoresInd):
    """Escolhe o melhor indivíduo e o passa para a próxima geração"""
    Populacao = sorted(Populacao, key=lambda i: i['fitness'], reverse=True)
    NewPOP.append(Populacao[0])
    MelhoresInd.append(Populacao[0])


def mutacao(gene):
    """Muta os bits para o valor oposto com base em uma taxa de mutação"""
    for i, b in enumerate(gene):
        if random.random() > hp.TAXA_MUTACAO:
            gene[i] = abs(gene[i]-1)

    return gene


def cruzamento(pai1, pai2):
    """Dados dois pais, realiza o cruzamento com o método de dois pontos aleatórios"""

    #Realiza o sorteio dos pontos aleatórios
    pontos = [random.randint(0, 16), random.randint(0, 16)]
    pontos = sorted(pontos)

    filho1 = {}
    filho2 = {}


    #Concatena os bits do gene X
    #Pegando de 0 até o primeiro ponto do Pai 1
    # do ponto 1 até o ponto 2 do Pai 2
    # do ponto 2 até o ultimo bit do Pai 1
    aux = pai1['Xbin'][:pontos[0]] + \
        pai2['Xbin'][pontos[0]:pontos[1]] + pai1['Xbin'][pontos[1]:]

    #Realiza a a mutação do gene criado
    filho1['Xbin'] = mutacao(aux)

    #Gene X para Filho 2
    aux = pai2['Xbin'][:pontos[0]] + \
        pai1['Xbin'][pontos[0]:pontos[1]] + pai2['Xbin'][pontos[1]:]
    filho2['Xbin'] = mutacao(aux)
    
    #Gene Y para Filho 1
    aux = pai1['Ybin'][:pontos[0]] + \
        pai2['Ybin'][pontos[0]:pontos[1]] + pai1['Ybin'][pontos[1]:]
    filho1['Ybin'] = mutacao(aux)
    
    #Gene Y para Filho 2
    aux = pai2['Ybin'][:pontos[0]] + \
        pai1['Ybin'][pontos[0]:pontos[1]] + pai2['Ybin'][pontos[1]:]
    filho2['Ybin'] = mutacao(aux)


    #Adequação dos filhos ao intervalo
    dc.indLimits(filho1)
    dc.indLimits(filho2)

    #Fitness Do filhos
    dc.indDecode(filho1)
    filho1['fitness'] = dc.calc(filho1['Xdec'], filho1['Ydec'])

    dc.indDecode(filho2)
    filho2['fitness'] = dc.calc(filho2['Xdec'], filho2['Ydec'])

    return filho1, filho2


def novaPop(NewPOP, nElementos, Populacao, MelhoresInd):
    
    #Limpa a NewPOP para inserção de novos individos
    NewPOP.clear()

    #Pega o melhor individuo da população e adiciona a proxima geração
    elitismo(Populacao, NewPOP, MelhoresInd)

    #Iterações até a proxima geração ter a mesma
    #quantidade de individuos que a atual, mantendo sempre a mesma quantidade
    #em todas as gerações
    while len(NewPOP) < nElementos:
        p1 = seleciona(Populacao)
        p2 = seleciona(Populacao)

        #ganrante que os pais são individuos diferentes
        while p1 == p2:
            p2 = seleciona(Populacao)


        if random.random() < hp.TAXA_CRUZAMENTO:
            filho1, filho2 = cruzamento(p1, p2)
        else:
            filho1 = p1
            filho2 = p2

        NewPOP.append(filho1)

        #Caso a população já tenha atigindo seu limite
        #Elimina o segundo filho
        if len(NewPOP) == nElementos:
            break
        else:
            NewPOP.append(filho2)

    return NewPOP
