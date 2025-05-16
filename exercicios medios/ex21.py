
numeros = []
pares = []

for i in range(10):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    if i % 2 == 0:
        numeros.remove(i)

numeros_sem_pares = numeros.remove(i)
print(numeros_sem_pares)