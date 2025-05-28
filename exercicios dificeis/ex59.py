
far = [int((celsius * 1.8) + 2) for celsius in [int(x) for x in input('Digite a temperatura atual em celsius: ').split()]]
print(f'A temperatura em Fahrenheit é: {far}')