from random import randint
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


random_number = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))

print(random_number)
print(f'O maior número foi: {max(random_number)}')
print(f'O menor número foi: {min(random_number)}')
