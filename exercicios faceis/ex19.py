'''
 Solicite nomes até que o usuário digite ”sair”. Armazene em uma lista e imprima.
'''

def nomes():

    nomes = []

    while True:
        nome = input('Digite seu nome (ou sair): ')
        if nome.lower() == 'sair':
            break
        else:
            nomes.append(nome)

    return nomes
print(nomes())