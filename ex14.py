# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]
valor = 0

for c in range(1, 8):
    valor = (int(input(f"digite o {c}º valor: ")))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print()
print('x~' * 30)
print()
valores[0].sort()
valores[1].sort()
print(f'Os valores pares são {valores[0]}')
print(f'Os valores ímpares são {valores[1]}')