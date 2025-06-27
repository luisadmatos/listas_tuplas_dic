

def dados_pessoas():
    for pessoa in dados:
        print(f'\nNome: {pessoa['nome']}')
        print(f'Idade: {pessoa['idade']}')
        print(f'Cidade: {pessoa['cidade']}')

dados = [
    {'nome': 'Julia', 'idade':20, 'cidade': 'Três Lagoas'},
    {'nome': 'Guilherme', 'idade': 20, 'cidade': 'Farroupilha'},
    {'nome': 'Adriele', 'idade': 20, 'cidade': 'Santa Maria'}
]

print('\n DADOS')

dados_pessoas()
