
numeros = []

for i in range(10):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)

print(numeros)  