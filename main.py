import hiperparametros as hp
import imagens
import gerarnovapopulacao as Newpop
import decodeecontrole as dc
import PrimeiraPOP

nElementos = int(input('Quantos indivíduos por geração? '))
geracoes = int(input('Quantas gerações? '))


Populacao = list()
NewPOP = list()
MelhoresInd = list()


PrimeiraPOP.PopulacaoInicial(nElementos, Populacao)

imagens.limpaHistorico()

#Iterações até a o número de gerações
for g in range(geracoes):
    if g%hp.quantidadeDeImagens(geracoes) == 0:
        imagens.imgGeracao(Populacao, g)
    NewPOP = Newpop.novaPop(NewPOP, nElementos, Populacao, MelhoresInd)
    Populacao = NewPOP[:]

imagens.GraficoEvolucaoDoFitness(sorted(MelhoresInd, key=lambda i: i['fitness']))
