valida_media = False
aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()

while valida_media != True:
    aluno['media'] = float(input('Média: '))

    if aluno['media'] < 0 or aluno['media'] > 10:
        print('Valor da média inválido. Tente novamente.')
    else:
        if aluno['media'] < 7:
            aluno["situacao"] = 'Reprovado'
        else:
            aluno["situacao"] = 'Aprovado'
        
        valida_media = True

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')