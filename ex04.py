# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')))

print(f'Os números sorteados foram {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vez(es)')
if numeros == 3:
    print(f'O número 3 está na {numeros.index(3) + 1}ª posição.')
else:
    print('Não ecxiste número 3')
print(f'Os números pares é (são) ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
