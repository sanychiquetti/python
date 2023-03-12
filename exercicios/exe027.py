"""
Faça um programa que leia o nome completo de uma pessoa, e mostre o primeiro nome e o último nome
separadamente.
Ex: Ana Maria de Souza
primeiro nome: Ana
último nome: Souza
"""
nome = input('Qual seu nome completo? ').strip()
primeiroNome = nome.split()
print('Seu primeiro nome é {}'.format(primeiroNome[0]))
print('Seu último nome é {}'.format(primeiroNome[len(primeiroNome)-1])) #aqui estou pegando o comprimento dela -1, vai dar o ultimo nome