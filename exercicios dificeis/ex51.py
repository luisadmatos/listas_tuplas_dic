
fila = []

while True:
    print('\n MENU ')
    print('1. Chegada do cliente')
    print('2. Atender cliente')
    print('3. Mostrar fila')
    print('4. Sair')

    opcao = input('Escolha uma opção:')

    if opcao == '1':
        cliente = input('Digite o nome do cliente: ')
        fila.append(cliente)
    elif opcao == '2':
        if fila:
            cliente = fila.pop(0)
            print(f'Atendendo {cliente}')
        else:
            print('Nenhum cliente na fila')
    elif opcao == '3':
        if fila:
            print(f'Fila atual: {fila}')
        else: 
            print('Não há ninguém na fila')
    elif opcao == '4':
        print('Encerrando...')
        break
    else: 
        print('Opção inválida. Tente novamente')