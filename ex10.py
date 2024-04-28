# Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('x~' * 30)
print(f'\nForam digitados {len(lista)} números.')
print(f'Os valores digitados foram {lista}')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente foram {lista}')
if 5 in lista:
    print(f'O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
