# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

unica = ('pão', 9.90, 'mussarela', 9.80, 'hamburguer', 65.00)

print('-=' * 30)
print('                   LISTAGEM DE PREÇOS')
print('-=' * 30)

for item in range(0, len(unica)):
    if item % 2 == 0:
        print(f'   {unica[item]:.<30}',end='')
    else:
        print(f'{unica[item]:.>22}')

print('-=' * 30)
