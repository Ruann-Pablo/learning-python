lista = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in lista:
        print('Valor duplicado! Valor não adicionado a lista.')
    else:
        lista.append(valor)

    resposta  = str(input('Quer continuar? [S/N]: ')).strip().lower()

    if resposta == 'n':
        break

lista.sort()

print(f'Você digitou os valores: {lista}')