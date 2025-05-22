
numeros = [1, 2, 3, 4, 5, 6]

if len(numeros) >= 2:
    primeiro = max(numeros)
    numeros.remove(primeiro)

    segundo = max(numeros)
    print(f'O segundo maior numero da lista é: {segundo} ')