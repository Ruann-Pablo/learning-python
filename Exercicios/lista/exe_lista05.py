lista = []
lista_par = []
lista_impar = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    while True:
        resposta = input('Quer continuar? [S/N]: ').strip().lower()
        if resposta in ('s', 'n'):
            break
        print('Comando inválido. Tente novamente.')
 
    if resposta == 'n':
        break

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

print('-' *30)
print(f'Lista completa: {lista}')
print(f'Lista com os valores pares: {lista_par}')
print(f'Lista com os valores impares: {lista_impar}')
