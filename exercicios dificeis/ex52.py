
lista_strings = ['lucas', 'any', 'guilherme', 'luisa', 'aaaaaa']

lista_strings.sort(key=lambda palavra: sum(1 for letra in palavra.lower() if letra in 'aeiou'))

print(lista_strings)