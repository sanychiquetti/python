"""
Faça um programa que leia o nome completo de uma pessoa, e mostre o primeiro nome
e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro nome: Ana
último nome: Souza
"""
nome = input('Qual seu nome completo? ')
primeiroNome = nome.split()
print('Seu primeiro nome é {}'.format(primeiroNome[0]))
print('Seu último nome é {}'.format(primeiroNome[3]))