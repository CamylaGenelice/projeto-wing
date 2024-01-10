# Usando o split para criar uma lista de texto
'''
n = 'camyla linda demais '
x = n.split()
for c, i in enumerate(x):
    print(f"indice: {c+1} elemento: {i} ") 
def pot (base,expo):
    s = pow(base,expo)
    print(s)

pot(2,3) '''

#import  numpy as np
import matplotlib.pyplot as plt

# Definindo os pontos
P_0 = np.array([-2, 1])
P_1 = np.array([5, 3])
P_2 = np.array([-3, -7])
P_3 = np.array([0, 1])

# Definindo o número de pontos na curva de Bézier
N = 100

# Inicializando a lista de pontos
P = np.zeros((N, 2))

# Calculando os pontos na curva de Bézier
for K in range(N):
    t = K / N
    P[K] = (1-t)**3 * P_0 + 3*(1-t)**2 * t * P_1 + 3*(1-t) * t**2 * P_2 + t**3 * P_3

# Plotando os pontos e a curva de Bézier
plt.figure()
plt.plot([P_0[0], P_1[0]], [P_0[1], P_1[1]], 'r-')
plt.plot([P_1[0], P_2[0]], [P_1[1], P_2[1]], 'r-')
plt.plot([P_2[0], P_3[0]], [P_2[1], P_3[1]], 'r-')
plt.plot(P[:,0], P[:,1], 'b-')
plt.scatter([P_0[0], P_1[0], P_2[0], P_3[0]], [P_0[1], P_1[1], P_2[1], P_3[1]], color='red')
plt.show()





