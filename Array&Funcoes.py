# Soma de vetores

import numpy as np
"""
v = np.array([1,2,3])
u = np.array([2,6,3]) #negativo
vu = np.array([])
sub = v - u
vu = np.append(vu,sub)
print(vu)

#FUNÇÃO
def soma_vetores(a,b):
    ab = np.array([])
    sub = b - a
    ab = np.append(ab,sub)
    print('A subtração dos arrays {}, {} resultou no array {}'.format(a,b,ab))


a = np.array([4,3,1])
b = np.array([8,2,1])
soma_vetores(a,b)
"""

vetor1 = np.array([[1,5,4],[9,3,8]])
vetor2 = np.array([[6,1,5],[7,3,9]])

for i in vetor1:
    for a in vetor2:
        multi = i * a + 
        resultado = np.array([[]])
        resultado = np.append(resultado,multi)
    print(multi)