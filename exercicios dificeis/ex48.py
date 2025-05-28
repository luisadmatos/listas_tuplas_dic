
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
pares_quadrado = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    
for par in pares:
    quadrado = par ** 2
    pares_quadrado.append(quadrado)

print(pares_quadrado)