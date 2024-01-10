#jogo
# personagens Maya, Marcus e Fel
#Inicio do jogo
def racional(n):
    contador = 1  # Inicialize o contador de posição do número racional
    p = 1  # posição inicial da linha
    q = 1  # posição inicial da coluna
    while contador < n:
        if p == 1 and q % 2 != 0:  # Se p=1 e q é ímpar
            q += 1
            contador += 1
        elif p == 1 and q % 2 == 0:  # Se p=1 e q é par
            while q != 1 and contador < n:
                p += 1
                q -= 1
                contador += 1
        elif q == 1 and p % 2 == 0:  # Se q=1 e p é par
            p += 1
            contador += 1
        elif q == 1 and p % 2 != 0:  # Se q=1 e p é ímpar
            while p != 1 and contador < n:
                p -= 1
                q += 1
                contador += 1

    return p, q

# Testando a função com um valor de n:
print(racional(1000000))
