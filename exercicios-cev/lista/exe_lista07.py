lista_grupo = []
lista_pessoa = []
maior_peso = 0
menor_peso = 0

while True:
    lista_pessoa.append(str(input('Nome: ')).strip().title())
    lista_pessoa.append(int(input('Peso: ')))

    if len(lista_grupo) == 0:
        maior_peso = lista_pessoa[1]
        menor_peso = lista_pessoa[1]
    else:
        if lista_pessoa[1] > maior_peso:
            maior_peso = lista_pessoa[1]

        if lista_pessoa[1] < menor_peso:
            menor_peso = lista_pessoa[1]

    lista_grupo.append(lista_pessoa[:])
    lista_pessoa.clear()

    while True:
        resposta = input('Quer continuar? [S/N]: ').strip().lower()
        if resposta in ('s', 'n'):
            break
        print('Comando inválido. Tente novamente.')
 
    if resposta == 'n':
        break

print('-' *40)
print(f'Ao todo você cadastrou {len(lista_grupo)} pessoas.')
print(f'O maior peso registrado foi de: {maior_peso}. Individuo(s) com este peso: ', [p[0] for p in lista_grupo if p[1] == maior_peso])
print(f'O menor peso registrado foi de: {menor_peso}. Individuo(s) com este peso: ', [p[0] for p in lista_grupo if p[1] == menor_peso])

'''
User: @adryelbarros3250
Descobri que dá pra usar o for da mesma forma que quando usa o enumerate(), por exemplo:

feito no código:
`for p in lista_grupo:
    if p[1] == menor_peso:
        print(p[0], end=' ')
`

dá pra fazer assim também:
`for nome, peso in princ:
    if peso == men:
        print(nome, end=' ')
`
Como cada item de princ tem dois valores, o primeiro valor vai pra 'nome' e o segundo, pra 'peso' 
'''