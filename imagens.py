from matplotlib import pyplot as plt
import os

def limpaHistorico():
    """Exclui todas as imagens presentes na pasta 'graficos'"""
    if os.path.isdir("./graficos"):
        for arquivo in os.listdir("./graficos/"):
                os.remove("./graficos/" + arquivo)
    else:
        os.mkdir("graficos")

def imgGeracao(Populacao, g):
    """Gera e salva um gráfico de dispersão dos indivíduos da população atual"""
    
    listX = list()
    listY = list()
    for ind in Populacao:
        listX.append(ind['Xdec'])
        listY.append(ind['Ydec'])

    plt.xlim([0, 0.5])
    plt.ylim([0, 0.5])
    plt.scatter(listX, listY)
    plt.title(f"Indivíduos da geração {g}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig(f"./graficos/{g}")
    plt.close()

def GraficoEvolucaoDoFitness(MelhoresInd):
    """Gera e salva um gráfico que exibe a evolução do melhor fitness por geração"""
    dados = []
    for i, ind in enumerate(MelhoresInd):
        dados.append(ind['fitness'])
    print("\n Melhor individuo:\n")
    print(MelhoresInd[-1])

    plt.plot(range(len(dados)), dados)
    plt.grid(True, zorder=0)
    plt.title("Elitismo do fitness")
    plt.xlabel("Gerações")
    plt.ylabel("Valor do fitness")
    plt.savefig("./graficos/elitismoFitness.jpg")
    plt.show()