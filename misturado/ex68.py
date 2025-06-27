'''
 Converta uma lista de tuplas (chave, valor) em um dicionário.
'''

def dic_lista_tupla():

    lista = []

    while True:
        nome = input('Digite o nome do produto ou sair para encerrar: ')
        if nome.lower() == 'sair':
            print('Saindo...')
            break

        try:
            preco = int(input('Digite o valor do produto: '))
            lista.append((nome, preco))
        except ValueError:
            print('Valor inválido. Tente novamente')


    dicionario_tuplas = dict(lista)
    return dicionario_tuplas

produtos = dic_lista_tupla()    
print(produtos)