
numeros = [2, 4, 6, 8, 10, 12, 14]
inicio = 0
fim = len(numeros) - 1
escolhido = int(input('Digite o número da sua escolha: '))
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if numeros[meio] == escolhido:
        print(f'O valor {escolhido} foi encontrado na posição {meio}. ')
        encontrado = True
        break
    elif numeros[meio] < meio:
        inicio = meio + 1
    else:
        fim = meio - 1
if not encontrado:
    print('Atenção: valor não encontrado')    