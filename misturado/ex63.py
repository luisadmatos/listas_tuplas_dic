
pares = {}

def preco_produto():

    n = int(input('Quantos produtos deseja cadastrar? '))

    for _ in range(n):
        produto = input('Digite o nome do produto: ')
        preco = int(input('Digite o preço do produto: '))
        pares[produto] = preco

def encontrar_produtos(pares, produto):
    if produto in pares:
         return f"O preço de {produto} é R$ {pares[produto]:.2f}"
    else:
        return f'O produto {produto} não foi encontrado!'


preco_produto()

while True:
    busca = input('Digite o nome do produto para pesquisar (ou "sair" para encerrar): ')
    if busca.lower() == 'sair':
        print("Encerrando pesquisa.")
        break
    print(encontrar_produtos(pares, busca))