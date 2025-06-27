'''
Use um laçoo while para imprimir os elementos de uma lista um por um.
'''
def elementos_por_vez():

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 0

    while i < len(lista):
        print(lista[i])
        i += 1

elementos_por_vez()    