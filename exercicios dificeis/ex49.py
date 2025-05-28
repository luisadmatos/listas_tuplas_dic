
lista = [10, 9, 8, 7, 6]
n = 3

n = n % len(lista)
lista = lista[-n:] + lista[:-n]

print(lista)