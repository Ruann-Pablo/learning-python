lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_coluna = 0
maior_seglinha = 0

for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        
        if  lista[i][j] % 2 == 0:
            soma_par += lista[i][j]
        
        if j == 2:
            soma_coluna += lista[i][j]

        if i == 1:
            if lista[i][j] > maior_seglinha:
                maior_seglinha = lista[i][j]

print('-' * 30)

for i in range(len(lista)):
    for j in range(len(lista)):
        print(f'[{lista[i][j]}]', end='')
    print()

print('-' * 30)
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior_seglinha}')