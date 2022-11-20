from math import ceil

TAXA_MUTACAO = 0.98
TAXA_CRUZAMENTO = 0.9
PORCENTAGEM_DE_IMAGENS = 100

def quantidadeDeImagens(geracoes):
    return ceil(geracoes/ceil(geracoes*(PORCENTAGEM_DE_IMAGENS/100)))