'''Exercicio de lista  '''
lista = []
'''
while True:
    n = int(input("Digite um número: "))
    s = str(input('quer continuar S/N ?'))
    lista.append(n)
    if s.lower() == 'n':
        break
    
if n == 5 in lista:
    print('O valor 5 esta na lista ')
    
else: 
    print('O valor 5 não esta na lista')

list2 = sorted(lista, reverse=True) 
print(list2) 
print('A quantidade de numeros na lista {}'.format(len(lista))) '''




'''
lista = []

for c in range(0,5):
    n = int(input('Digite um número '))
    if c == 0 or n > lista[len(lista)-1]: # Se o número for maior ou o primeiro, ele é adicionado no final da lista.
        lista.append(n) 
        print('O número foi adicionado ao final da lista ')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n) 
                print('O número foi adicionado na posição {} '.format(pos))
                break
            pos += 1
print('---'*22)
print(lista) '''


'''
nome = str(input('Digite seu nome: '))
i = int(input('Digite sua idade: '))
print('Ola, meu nome é {} e eu tenho {} anos '.format(nome,i)) 

lista = ['mamão', 'banana', 'uva','pera', 'maçã']
for c in range(2):
    n = str(input('Digite o nome de uma fruta: '))
    lista.append(n)
print(lista) '''

'''
lista = []
for c in range (1,11):
    
    if c % 2 != 0:
        lista.append(c)
        print(c)'''
'''
def tes (a): 
    s = a**2 
    print(s)

n = int(input('digite um numero: '))
tes(n) '''
#print(tes(3)) modo errado
i = 1
lista = []
while i <= 10:
    #print(i)
    lista.append(i)
    i += 1
s = 0
for c in range(len(lista)):
    s = sum(lista)
print(s)
print(lista)