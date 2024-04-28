#  Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#  (largura e comprimento) e mostre a área do terreno.
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg:.2f} metros por um terreno de {comp:.2f} metros é de '
          f'{a:.2f} metros quadrados.')


l = float(input('Largura do terreno: '))
c = float(input('Comprimento do terreno: '))
área(l, c)
