#  Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
#  mostre uma mensagem com tamanho adaptável. Ex: escreva(‘Olá, Mundo!’) Saída:
#   ~~~~~~~~~
#  Olá, Mundo!
#   ~~~~~~~~~

def txt(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


txt('FIADO SÓ AMANHÃ')
txt('tá sabendo legal')
