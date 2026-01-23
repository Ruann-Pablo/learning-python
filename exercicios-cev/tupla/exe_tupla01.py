tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    resposta = int(input('Digite um número entre 0 e 10: '))

    if resposta < 0 or resposta > 10:
        print('Número inválido. Tente novamente.')
    else:
        print(f'Você digitou o número {tupla[resposta]}.')
        break
    

