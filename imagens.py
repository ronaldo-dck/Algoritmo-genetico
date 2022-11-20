from PIL import Image
from matplotlib import pyplot as plt


def make_gif(geracoes):
    frames = list()
    for i in range(geracoes):
        frames.append(Image.open(f'./teste/output{i}.jpg'))
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames, save_all=True, duration=250, loop=1)


def imgGeracao(Populacao, g):
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
    plt.savefig(f"./teste/output{g}.jpg")
    plt.close()

def GraficoEvolucaoDoFitness(MelhoresInd):
    dados = []
    for i, ind in enumerate(MelhoresInd):
        dados.append(ind['fitness'])
    print(MelhoresInd[-1])

    plt.plot(range(len(dados)), dados)
    plt.grid(True, zorder=0)
    plt.title("Elitismo do fitness")
    plt.xlabel("Gerações")
    plt.ylabel("Valor do fitness")
    plt.show()