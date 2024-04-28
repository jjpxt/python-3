# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valores duplicado não será adicionado.')
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
numeros.sort()
print(f'Voce digitou os números {numeros}')
