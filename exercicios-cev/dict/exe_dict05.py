construtor_usuario = {}
lista_usuarios = []
soma_idade = 0
media_idade = 0

while True:
    construtor_usuario["nome"] = str(input('Nome: ')).title().strip()
    
    while True:
        construtor_usuario["sexo"] = str(input('Sexo [M/F]: ')).upper().strip()
        if construtor_usuario["sexo"] in ('M', 'F'):
            break
        print('Sexo inválido. Tente novamente.')
            
    while True:
        construtor_usuario["idade"] = int(input('Idade: '))
        if construtor_usuario["idade"] in range(0, 120):    
            break
        print('Idade inválida. Tente novamente.')

    while True:
        resposta = input('Quer continuar? [S/N]: ').lower().strip()
        if resposta in ('s', 'n'):
            break
    
    lista_usuarios.append(construtor_usuario.copy())

    if resposta == 'n':
        break

print('-='*30)
print(f'A) Ao todo temos {len(lista_usuarios)} pessoas cadastradas.')

for usuario in lista_usuarios:
    soma_idade += usuario["idade"]
media_idade = soma_idade / len(lista_usuarios)

print(F'B) A média de idade é de: {media_idade:.1f} anos.')
print(f'C) As mulheres cadas tradas foram: ', end='')

for usuario in lista_usuarios:
    if usuario["sexo"] != 'M':
        print(usuario["nome"], end=', ')
print()

print(f'Lista de pessoas acima da média: ')

for usuario in lista_usuarios:
    if usuario["idade"] > media_idade:
        for c, v in usuario.items():
            print(f'=> {c} = {v}', end=' | ')
        print()