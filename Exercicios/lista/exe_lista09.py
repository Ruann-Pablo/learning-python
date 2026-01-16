lista = [[[], [], []], [[], [], []], [[], [], []]]
# lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        lista[i][j].append(valor)


for i in range(len(lista)):
    for j in range(len(lista)):
        print(lista[i][j], end='')
    print()

        
    