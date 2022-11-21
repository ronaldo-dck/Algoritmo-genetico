import hiperparametros as hp
import imagens
import gerarnovapopulacao as Newpop
import decodeecontrole as dc
import PrimeiraPOP

nElementos = 200
geracoes = 200


Populacao = list()
NewPOP = list()
MelhoresInd = list()


PrimeiraPOP.PopulacaoInicial(nElementos, Populacao)
imagens.limpaHistorico()

#Evolução
for g in range(geracoes):
    if g%hp.quantidadeDeImagens(geracoes) == 0:
        imagens.imgGeracao(Populacao, g)
    NewPOP = Newpop.novaPop(NewPOP, nElementos, Populacao, MelhoresInd)
    Populacao = NewPOP[:]

imagens.GraficoEvolucaoDoFitness(sorted(MelhoresInd, key=lambda i: i['fitness']))
