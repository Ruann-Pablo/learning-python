aluno_nota = []
lista_alunos = []

def nota_func():
    notas_list = []
    cont = 0

    while cont < 2:
        nota = float(input(f'Nota {cont + 1}: '))

        if nota < 0 or nota > 10:
            print('Nota inválida. Serão permitidas apenas notas de 0 à 10.')
        else:
            notas_list.append(nota)
            cont += 1

    return notas_list
    
while True:
    soma_notas = 0.0
    media = 0.0

    print('-' * 30) # estético
    aluno_nota.append(str(input('Nome: ')).strip().title())
    aluno_nota.append(nota_func())

    for i in range(2):
        soma_notas += aluno_nota[1][i]
    
    media = soma_notas / len(aluno_nota[1])
    
    aluno_nota.append(media)

    lista_alunos.append(aluno_nota[:])
    aluno_nota.clear()

    while True:
        resposta = input('Quer continuar? [S/N]: ').strip().lower()
        if resposta in ('s', 'n'):
            break
        print('Comando inválido. Tente novamente.')
 
    if resposta == 'n':
        break

while True:
    print('-=' * 15) # estético
    print(f'ID | {"NOME":^10} | MEDIA"') # estético
    print('-' * 30) # estético
    
    for i in range(len(lista_alunos)):
        print(f'{i} | {lista_alunos[i][0]:^10} | {lista_alunos[i][2]}')

    while True:
        print('-' * 30) # estético
        ver_nota = int(input('Mostrar nota do aluno [999 interrompe o programa]: '))
        
        if ver_nota == 999:
            break
        
        print(f'Aluno(a): {lista_alunos[ver_nota][0]}\nNotas: {lista_alunos[ver_nota][1]}')

    if ver_nota == 999:
        break