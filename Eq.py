"""
l = [1,2,3,4,5]
for c in l:
    print(c)

lista = [1, 2, 3, 4, 5,6,7,8,9]
for c in reversed(lista):
    print(c)
"""

""" 
lista = []
s = 0
for c in range(4):
    n = int(input('Digite sua nota '))
    lista.append(n)
    s = sum(lista)/2
print(s)
print(lista)"""
#from itertools import groupby

"""Esse trecho de código verifica se nas duas listas tem elementos iguais
consoantes = ['c','d','f','g','o']
mix = ['g','a','e','d','c','o','i','u']
lista = []
for i in consoantes:
    for m in mix:
        if i == m:
            lista.append(i)
            print(lista)
função 
def verifica (a,b):
    lista = []
    for i in a:
        for m in b:
            if i == m:
                lista.append(i)
    print(lista) 

consoantes = ['c','d','f','g','o']
mix = ['g','a','e','d','c','o','i','u']
verifica(mix,consoantes)  """

def verifica (a,b):
    lista_p = []
    lista_i = []
    for i in a:
        d = i % 2
        if d == 0:
            lista_p.append(i)
        else:
            lista_i.append(i)
    for c in b:
        div = c % 2
        if div == 0:
            lista_p.append(c)
        else:
            lista_i.append(c)
    # Removendo os numeros duplicados. Transformando a lista em dicionário e transformando o dicionário em lista novamente.
    # Não usei a função set() pois a função altera a ordem dos elementos, e eu não quero isso.
    convert_dic_lista1 = list(dict.fromkeys(lista_p))
    convert_dic_lista2 = list(dict.fromkeys(lista_i))
    print(convert_dic_lista1)
    print(convert_dic_lista2)




lista1 = [12,33,44,4,17,16,23,6,5,57,35,90,88,21,12,16,24,24,22,22]
lista2 = [6,5,4,56,8,9,14,17,88,37,54,20,21,72]

verifica(lista1,lista2)















