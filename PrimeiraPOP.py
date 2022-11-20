from random import randint
import decodeecontrole as dc

def PopulacaoInicial(nElementos, Populacao):
    for i in range(nElementos):
        individuo = {'Xbin': gerarGene(), 'Ybin': gerarGene(),
                    'Xdec': 0.0, 'Ydec': 0.0, 'fitness': 0.0}
        individuo['Xdec'] = dc.decode(individuo['Xbin'])
        individuo['Ydec'] = dc.decode(individuo['Ybin'])
        individuo['fitness'] = dc.calc(individuo['Xdec'], individuo['Ydec'])
        Populacao.append(individuo)
    return Populacao    


def gerarGene():
    """gera aleatoriamente uma sequencia de 16 bits, que então é adequada para o intervalo desejado"""
    gene = [randint(0, 1) for x in range(16)]
    dc.limiar(gene)
    return gene
