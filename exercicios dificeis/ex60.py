'''
 Implemente um sistema de cadastro de usu´ arios com login, utilizando listas de
 tuplas.
'''
usuarios = []

while True:
    print('\n MENU ')
    print('1. Cadastro de usuário')
    print('2. Login')
    print('3. Sair')

    opcao = input('Escolha uma das opções acima: ')

    if opcao == '1':
        username = input('Digite o nome do usuário: ')
        existe = False
        for nome, _ in usuarios:
            if nome == username:
                print('Usuário existente')
                existe = True
                break
        if not existe:
            senha = input('Digite a senha: ')
            usuarios.append((username, senha))
            print('Usuário cadastrado!')
    elif opcao == '2':
        username = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')
        logado = False
        for nome, tent in usuarios:
            if nome == username and tent == senha:
                print('Login realizado com sucesso!')
                logado = True
                break
        if logado:
            break
        else:
            print('Usuário ou senha incorretos')
    elif opcao == '3':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente')