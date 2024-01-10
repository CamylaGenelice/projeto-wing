import networkx as nx
import matplotlib.pyplot as plt

# fonte vai ser o local de partida, onde o algoritmo vai calcular da fonte ate os outros nós
def dij (grafo,fonte):
    global vertice_atual
    distancias = {no: float('inf') for no in grafo}
    predecessores = {no: 'und' for no in grafo}
#predecessores vai pegar todos os nós que estão no grafico e vai jogar para indefinido

    #lista de vertices
# Vai selecionar o nó que tiver a menor distancia.
# Depois de selecionado o nó vai ser removido e não vai fazer parte da proxima iteração
    ver = [no for no in grafo]
# Especificando que a distancia da fonte para ele mesmo é zero e que o seu predecessor é ele mesmo.

    distancias[fonte] = 0
    predecessores[fonte] = fonte

#Implementação da rotina
    while len(ver) > 0:
        #seleciona o vertice com a menor distancia
        s = float('inf')
        for no in ver:
            if distancias[no] < s:
                s = distancias[no]
                vertice_atual = no

        ver.remove(vertice_atual)

        for vizinho, peso in grafo[vertice_atual].items():
            alt = distancias[vertice_atual] + peso
            #Atualizando a distancia calculada
            if distancias[vizinho] > alt:
                distancias[vizinho] = alt
                predecessores[vizinho] = vertice_atual
    return distancias, predecessores

# dicionario
grafo = {
    "A": {"B": 1 , "C": 4},
    "B": {"A": 1, "C": 1, "D": 3, "E": 5},
    "C": {"A": 4, "B": 1, "D": 2, "E": 3},
    "D": {"B": 3, "C": 2, "E": 2},
    "E": {"B": 5, "C": 3, "D": 2}
}
source = 'A'
d,preve = dij(grafo,source)
print('Distâncias de cada nó: ',d)
print('=================================================================')
print('Predecessores: ',preve)
print('=================================================================')
# Função que determina o melhor caminho entre 2 vértices. Com base na função dij
def caminho (source, v):

    melhor_caminho = []
    melhor_caminho.append(v)
    predecessor = preve[v]
    melhor_caminho.append(predecessor)

    while predecessor != source:
        predecessor = preve[predecessor]
        melhor_caminho.append(predecessor)
    return sorted(melhor_caminho,reverse=True)

T = caminho(source, 'E')

print("Caminho para chegar de um nó ao outro", T)

g = nx.Graph(grafo)

for no in grafo:
    for vizinho, peso in grafo[no].items():
        g.add_edge(no,vizinho,weight = peso)

pos = nx.circular_layout(g)

nx.draw_networkx_nodes(g,pos)
nx.draw_networkx_labels(g,pos)
nx.draw_networkx_edges(g,pos, edgelist=[(v, p) for v, p in zip(T[:-1], T[1:])], edge_color='purple', width=2.0)
edge_labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g, pos,edge_labels)
plt.show()

