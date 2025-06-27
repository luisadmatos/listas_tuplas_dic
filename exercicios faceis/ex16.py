'''
Crie uma lista de 5 elementos e substitua o segundo elemento pelo valor 99.
'''

def substituir():

    numeros = [1, 2, 3, 4, 5]
    novo = 99

    indice = numeros.index(2)
    numeros[indice] = novo 

    return numeros

print(substituir())

