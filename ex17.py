# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'A média de {aluno["nome"]} foi: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
# elif 5 <= aluno['media'] < 7:
#     aluno['situação'] = 'RECUPERAÇÃO'
elif aluno['media'] >= 5:
    aluno['situação'] = 'RECUPERAÇÃO'
elif aluno['media'] < 5:
    aluno['situação'] = 'REPROVADO'

print(aluno)
