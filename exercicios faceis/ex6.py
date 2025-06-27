'''
 Solicite 5 números ao usuário e armazene em uma lista. Em seguida, imprima o
 maior e o menor número.
'''

def maior_menor():

    numeros = []

    for i in range(5):
        numero = int(input(f'Digite o {i+1}º numero: '))
        numeros.append(numero)

    print(max(numeros))
    print(min(numeros))

maior_menor()