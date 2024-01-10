import math
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy as sp

import networkx as nx
import matplotlib.pyplot as plt
import random

# Função para criar um grafo heterogêneo
def criar_grafo_heterogeneo(N):
    arestas = []
    Lista = [1, 2]
    arestas.append((1, 2))

    for i in range(3, N + 1):
        u = random.choice(Lista)
        arestas.append((i, u))
        Lista.extend([u, i])

    return arestas

# Função para o diâmetro do grafo
def calcular_diametro(grafo):
    try:
        return nx.diameter(grafo)
    except nx.NetworkXError:
        return "Infinito (grafo não conexo)"

# Entrada: N
N = 100

# Criar grafo heterogêneo
arestas_heterogeneo = criar_grafo_heterogeneo(N)
grafo_heterogeneo = nx.Graph()
grafo_heterogeneo.add_edges_from(arestas_heterogeneo)

# criação do grafo não-direcionado
grafo_aleatorio = nx.gnp_random_graph(N, p=math.log(N) / N)


layout = nx.kamada_kawai_layout(grafo_heterogeneo)

# Plote o grafo usando a biblioteca “matplotlib.pyplot”
nx.draw(grafo_heterogeneo, layout, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue", font_color="black", font_size=8)
plt.show()

# Chamando as funções
dia_heterogeneo = calcular_diametro(grafo_heterogeneo)
dia_aleatorio = calcular_diametro(grafo_aleatorio)


print(f"Diâmetro do grafo heterogêneo: {dia_heterogeneo}")
print(f"Diâmetro do grafo aleatório: {dia_aleatorio}")

# As vezes o diâmetro do grafo aleatório vai para o infinito
