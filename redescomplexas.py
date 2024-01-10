import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import math
import random


#número de vertices e probabilidade
nVertices = 100
probabilidade = math.log(nVertices)/nVertices
#grafo
g = nx.Graph

#lista

arestas = []

# Preencha a lista de arestas
for i in range(1, nVertices+1):
    for j in range(1,nVertices+1):
      if(j>i):
            num_aleatorio = np.random.rand() # gera um número aleatorio entre 0 e 1
            if(num_aleatorio > 1-probabilidade):
                arestas.append((i,j))

#



#função que desenha o grafico
grafo = nx.Graph()
grafo.add_edges_from(arestas)
layout = nx.spring_layout(grafo)




nx.draw(grafo,layout, with_labels=True, font_weight='bold', node_size = 700, node_color = "skyblue", font_color ="black", font_size = 8)
plt.show()





