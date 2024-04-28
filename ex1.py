# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até dez.
# Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.

numeros = 'ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ'


while True:
    num = int(input('Digite um número de zero até 10: '))
    if 0 <= num <= 10:
        break
    print('TENTE NOVAMENTE')
print(f'você escolheu o número {numeros[num]}')
