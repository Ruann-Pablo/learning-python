tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'O número 9 apareceu {tupla.count(9)}x.' if 9 in tupla else 'O número 9 não foi digitado')
print(f'O valor 3 apareceu na posição: {tupla.index(3)}.' if 3 in tupla else 'O número 3 não foi digitado')
print(f'Os valores pares ditados: ', end='')

for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end=' ')

