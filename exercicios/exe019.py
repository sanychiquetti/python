"""
Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo o nome sorteado.
"""
from random import choice
stud1 = str(input('1ª aluno: '))
stud2 = str(input('2ª aluno: '))
stud3 = str(input('3ª aluno: '))
stud4 = str(input('4ª aluno: '))
list = [stud1, stud2, stud3, stud4]
sort = choice(list)
print('The selected student was {} '.format(sort))
