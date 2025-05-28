
dicionario = {}

inicio = input('Digite palavras aleatórias: ')

palavras = inicio.split()

for palavra in palavras:
    tamanho = len(palavra)

    if tamanho in dicionario:
        dicionario[tamanho].append(palavra)
    else:
        dicionario[tamanho] = [palavra]

print('Palavras agrupadas por tamanho: ')
for tamanho, lista in dicionario.items():
    print(f'{tamanho} letras: {lista}')