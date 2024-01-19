# Código que realiza a soma de vetores e a subtração.

import numpy as np

v = np.array([1,2,3])
u = np.array([2,6,3]) #negativo
vu = np.array([])
sub = v + u # Variavel que vai receber a soma dos arrays.
vu = np.append(vu,sub) # Array que vai receber o resultado da soma.

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])
d = A+B
print(d)
print(vu)
"""
#Função que recebe dois pontos de uma reta e cria um vetor com esses dois pontos.
def novo_vetor(a,b):
    ab = np.array([])
    sub = b - a
    ab = np.append(ab,sub)
    print('A subtração dos arrays {}, {} resultou no array {}'.format(a,b,ab))


a = np.array([4,3,1])
b = np.array([8,2,1])
novo_vetor(a,b)
"""
