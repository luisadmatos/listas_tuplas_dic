
carrinho = {}
# 'Morango', 3.00, 'Chocolate', 7.99, 'Cheetos', 15.00
while True:
    print('\nCarrinho de Compras!')
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Total itens')
    opcao = int(input('Escolha uma opção (1-3):'))

    if opcao == 1:
        nome = input('O que deseja adicionar?')
        preco = float(input('Preço do item: R$ '))
        qtd = int(input('Quantidade: '))
        if nome in carrinho:
            carrinho[nome][1] += qtd
        else:
            carrinho[nome] = [preco, qtd]
        print(f'{qtd}x {nome} foram adicionados com sucesso!')

    elif opcao == 2:
        nome = input('O que deseja remover? ')
        if nome in carrinho:
            qtd = int(input('Quantidade: '))
            if carrinho[nome][1] > qtd:
                carrinho[nome][1] -= qtd
                print(f'{qtd}x {nome} removido(s). ')
            else:
                del carrinho[nome] 
                print(f'Todos {nome} removidos do carrinho')
        else:
            print('Item não encontrando')

    elif opcao == 3:
        if not carrinho:
            print('O carrinho está vazio.')
        else:
            total_itens = 0
            total_preco = 0
            print('\nItens do seu carrinho: ')
            for nome in carrinho:
                preco = carrinho[nome][0]
                qtd = carrinho[nome][1]
                subtotal = preco * qtd
            print(f'- {nome}: {qtd} x R${preco: .2f} = R${subtotal: .2f}')
    
    else:
        print('Opção inválida. Tente novamente')
        break
    