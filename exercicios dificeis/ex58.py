
numeros = [20, 45, 1, 56, 74, 12, 30, 1001]

num = [1] * len(numeros)

for i in range(len(numeros)):
    for j in range(i):
        if numeros[j] < numeros[i]:
            num[i] = max(num[i], num[j] + 1)

print(numeros)
print('Subsequência mais longa:', max(num))