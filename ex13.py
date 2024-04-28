# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
fdps = []
gordos = magros = 0
while True:
    pessoas.append(str(input('Qual seu nome? ')))
    pessoas.append(float(input('Qual seu peso? ')))
    if len(fdps) == 0:
        gordos = magros = pessoas[1]
    else:
        if pessoas[1] > gordos:
            gordos = pessoas[1]
        if pessoas[1] < magros:
            magros = pessoas[1] 
    fdps.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer parar? [S/N]'))
    if resp in 'Ss':
        break

print(f'Foram cadastradas {len(fdps)} pessoas.')
print(f'O maior peso foi {gordos:.2f} KGs. Peso de', end=' ')
for p in pessoas:
    if p[1] == gordos:
        print(f'[{p[0]}] ', end=' ')
print(f'\nO menor peso foi {magros:.2f} KGs. Peso de', end=' ')
for p in pessoas:
    if p[1] == magros:
        print(f'[{p[0]}] ', end=' ')
