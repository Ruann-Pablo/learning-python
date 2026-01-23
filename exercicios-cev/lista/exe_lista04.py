lista = []

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

lista.sort()
lista.reverse() # ou = lista.sort(reverse=True)

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores na ordem decrescente são: {lista}.')
print('O valor 5 faz parte da lista!' if 5 in lista else 'O valor 5 não faz parte da lista!')
