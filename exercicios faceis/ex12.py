
numeros = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}º numero: '))
    numeros.append(numero)
    if numero > 10:
        print('Número maior que 10')
