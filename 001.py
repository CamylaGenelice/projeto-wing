# Força e atrito

#(1)

def forca_aplicada(m:float,a:float):
    f = m*a
    print("A força aplicada que exerce em seu objeto é de: {}".format(f))

forca_aplicada(21.0,2.5)

#(2)

def achar_aceleracao():
    print('Esse código vai te ajudar a achar a aceleração do seu problema ;)')
    f = float(input('Digite a força: '))
    m = float(input('Digite a massa: '))
    a = f/m
    print('A aceleração do objeto é de:{} '.format(a))

achar_aceleracao()


