'''
Crie um dicionário que mapeia números de 1 a 5 para seus quadrados, usando laço for.
'''

quadrados = {}

def n_ao_quadrado():

    for i in range(1, 6):
        quadrados[i] = i ** 2

n_ao_quadrado()
print(quadrados)