'''
Crie uma lista de 5 letras e converta para uma única string com join
'''

def converter():

    letras = ['a', 'b', 'c', 'd', 'e']

    unica = ', '.join(letras)

    return unica

print(converter())