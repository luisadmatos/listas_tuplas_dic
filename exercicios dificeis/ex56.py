
matriz = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

for i in range(len(matriz)):
    soma = sum(matriz[i])
    print(f'Soma de cada linha {i + 1}: {soma}')