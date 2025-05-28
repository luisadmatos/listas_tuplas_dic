
inteiros = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10]
repetidos = []
count = []

for num in inteiros:
    con = inteiros.count(num)
    if con > 1 and num not in repetidos:
        repetidos.append(num)
        count.append(con)
    
for i in range(len(repetidos)):
    print(f'O número {repetidos[i]} aparece {count[i]} vezes')