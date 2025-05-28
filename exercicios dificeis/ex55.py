
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = ()

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] + numeros[j] == 10:
            pares.append((numeros[i], numeros[j]))

print(f'Os pares que somam 10 são: {pares}')