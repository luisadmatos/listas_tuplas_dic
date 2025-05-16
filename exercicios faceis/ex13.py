
numeros = []
pares = []

for i in range(1, 10):
    numeros.append(i)
    if i % 2 == 0:
        pares.append(i)

print(f'Números pares:{pares}')