# aça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor é {maior}')


maior(4, 32, 2, 1, 4, 6, 7, 8, 9)
maior(99, 3, 5, 666, 6, 6, 6, 6, 6, 6)
