'''
def t (a):
    if a % 2 == 0:
        print('numero par')
    else:
        print('numero impar')
        
t(271) '''

#Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota
'''
lista = [6,7,7,9]
soma = sum(lista) / 4

print('sua média final: ',soma)
print('Sua maior nota: ',max(lista))
print('Sua menor nota: ', min(lista)) '''

#Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"

lista = []
for c in range(1,5):
    n = int(input('Digite a {} nota: '.format(c)))
    lista.append(n)
    
media = sum(lista) / 4
print('A média foi: ',media)
if media >= 7:
    print('APROVADO!')
else: 
    nota_final = int(input('Nota da final: '))
    lista.append(nota_final)
    recalculando = sum(lista) / 5
    if recalculando >= 5:
        print('APROVADO!')
    else:
        print('REPROVADO!')


#print(lista)