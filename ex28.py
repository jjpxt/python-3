# aça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma–
# -  situação (opcional)

nome = (input('Qual seu primeiro nome: '))
if len(nome) <= 4:
    print('Seu nomé é pequeno.')
elif len(nome) <= 5 or nome <= 6:
    print('seu nome é normal.')
else:
    print('Seu nome é grande.')
