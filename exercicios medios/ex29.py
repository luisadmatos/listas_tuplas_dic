
lista = []

while True:
    print('\nMenu')
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Listar itens')
    print('4. Sair do menu')

    opcao = int(input('Escolha uma opção (1-4):'))

    if opcao == 1:
        add = input('O que deseja adicionar? ')
        lista.append(add)
        print('Item adicionado com sucesso!')
    elif opcao == 2:
        remover = input('O que deseja remover? ')
        if remover in lista:
            lista.remove(remover)
        else: 
            print('Item não encontrado')
    elif opcao == 3:
        print(lista)
    elif opcao == 4:
        print('Saindo do menu...')
        break
    else:
        input('Digite um número válido: ')

print(lista)