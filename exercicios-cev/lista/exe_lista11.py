from random import randint

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)

lista = []
salva_jogos = []
quant_jogos = int(input('Quantos jogos você quer sortear? Responda: '))

for i in range(1, quant_jogos + 1):
    # O ```_``` significa: “não me importo com esse valor, só quero repetir”. 
    lista = [randint(0, 60) for _ in range(6)] # Isso deixa o código semanticamente mais claro. Ao invés de usar ```j``` que será um valor.
    lista.sort()
    salva_jogos.append(lista)

for i, jogo in enumerate(salva_jogos):
    print(f'Jogo{i + 1}: {jogo}')

