from random import randint

jogador = {}
jogador_list = list()

print('Valores soretados:')
for i in range(0, 4):
    jogador['jogador'] = f'Jogador-{i + 1}'
    jogador['valor'] = randint(1, 6)

    jogador_list.append(jogador.copy())

    print(f'O {jogador["jogador"]} tirou {jogador["valor"]}')

print('-' * 40)

jogadores_org = sorted(jogador_list, key=lambda jg: jg["valor"], reverse=True)

for j in jogadores_org:
    print(f'{j["jogador"]} com {j["valor"]}')



# bubble-sort for value
# for i in range(len(jogador_list)):
#     for j in range(len(jogador_list)):
#         if jogador_list[i]["valor"] > jogador_list[j]["valor"]:
#             jogador_list[i], jogador_list[j] = jogador_list[j], jogador_list[i]
