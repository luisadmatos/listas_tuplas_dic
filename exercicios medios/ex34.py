
numeros = []

while True:
    num = int(input('Digite um número:'))

    if num < 0:
        break
    numeros.append(num)

media = sum(numeros) / len(numeros)
print(media)
