'''
 Crie uma lista com os números de 1 a 10 usando range() e imprima somente os
 pares.
'''

def numeros_pares():
    num = []

    for i in range(1,11):
        num.append(i)
    
    pares = list(filter(lambda x: x % 2 == 0, num))

    return pares

print(numeros_pares())