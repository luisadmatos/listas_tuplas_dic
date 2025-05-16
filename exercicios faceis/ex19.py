
nomes = []

while True:
    nome = input('Digite seu nome (ou sair): ')
    if nome.lower() == 'sair':
        break
    else:
        nomes.append(nome)

print('Nomes digitados:')
print(nomes)