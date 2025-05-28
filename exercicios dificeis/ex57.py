
lista1 = ['a', 'e', 'i', 'o', 'u']
lista2 = [1, 2, 3, 4, 5]

zip_manual = []

for i in range(min(len(lista1), len(lista2))):
    zip_manual.append((lista1[i], lista2[i]))

print(zip_manual) 