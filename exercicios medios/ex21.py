'''
Solicite ao usuário 10 números, armazene em uma lista e remova todos os números
 pares usando remove.
'''
numeros = []

def usar_remove():

    for _ in range(10):
        numero = int(input('Digite um numero: '))
        numeros.append(numero)

    tirar_pares = list(filter(lambda x: x % 2 != 0, numeros))

    return tirar_pares
      
print(usar_remove())  