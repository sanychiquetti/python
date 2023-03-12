"""
 O professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça
 um programa que leia o nome dos quatro alunos e mostre a ordem sorteada:
"""
from random import shuffle
stud1 = str(input('1º Aluno:'))
stud2 = str(input('2º Aluno:'))
stud3 = str(input('3º Aluno:'))
stud4 = str(input('4º Aluno:'))
lista = [stud1, stud2, stud3, stud4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)