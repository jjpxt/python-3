#  Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
#  só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! DIGITE UM NÚMERO VÁLIDO')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
