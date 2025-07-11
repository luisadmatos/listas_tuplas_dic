'''
Crie um sistema de agenda onde cada contato é uma chave e o valor é uma lista de
 telefones.
'''

def agenda():

    contatos = {
        'ana':[1234456, 47599661, 15476561],
        'carlos':[789654123, 7896511313, 44898561],
        'davi':[4575446, 544685641, 46846656]
    }

    return contatos.items()

for nome, numeros in agenda():
    print(f'{nome}: {numeros}')