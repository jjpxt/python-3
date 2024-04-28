# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('CURITIBA', 'BOTAFOGO', 'CUIABA', 'CRUZEIRO', 'INTERNACIONAL', 'GRÊMIO', 'VASCO', 'FLAMENGO', 'FLUMINENSE',
         'GOIAS', 'CHAPECOENSE', 'ATLETICO-GO')

print('-=' * 30)
print(times[0:5])
print('-=' * 30)
print(times[-4:])
print('-=' * 30)
print(sorted(times))
print('-=' * 30)
print(f'A chapecoense está na {times.index("CHAPECOENSE") + 1}ª posição.')
