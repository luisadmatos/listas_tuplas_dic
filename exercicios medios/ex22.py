'''
Crie uma função que recebe uma lista e retorna uma nova lista com apenas os
 elementos únicos.
'''

def elementos_unicos():

    lista = [4, 5, 5, 6, 6, 7, 8, 9, 10, 10]
    unicos = set(lista)
    
    return unicos

print(elementos_unicos())