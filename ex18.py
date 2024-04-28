# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
rank = list
print('VALORES SORTEADOS')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(rank)
for i, e in enumerate(rank):
    print(f'{i + 1}º lugar: {e[0]} com {e[1]}')
    sleep(1)
