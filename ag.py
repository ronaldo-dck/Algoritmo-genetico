import random
import math
import hiperparametros as hp
import imagens
import gerarnovapopulacao as Newpop
import decodeecontrole as dc
import PrimeiraPOP


nElementos = 100
geracoes = 50


Populacao = list()
NewPOP = list()
MelhoresInd = list()



PrimeiraPOP.PopulacaoInicial(nElementos, Populacao)

#Evolução
for g in range(geracoes):
    if g%hp.quantidadeDeImagens(geracoes) == 0:
     imagens.imgGeracao(Populacao, g)
    NewPOP = Newpop.novaPop(NewPOP, nElementos, Populacao, MelhoresInd)
    Populacao = NewPOP[:]



imagens.make_gif(geracoes)
imagens.GraficoEvolucaoDoFitness(sorted(MelhoresInd, key=lambda i: i['fitness']))
