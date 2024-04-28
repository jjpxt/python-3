# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('destemido', 'careca', 'executar', 'impossível', 'burros', 'devaneio', 'problemas', 'brasileira')

for item in palavras:
    print(f'\nna palavra {item.upper()} temos a(s) vogal(is) ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
