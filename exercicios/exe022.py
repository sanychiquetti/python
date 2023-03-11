"""
Crie um programa que leia um nome completo de uma pessoa e mostre:
O nome com todos as letras maiúsculas
O nome com todos as letras minúsculas
Quantas letras ao todo sem os espaços
Quantas letras tem o primeiro nome
"""
frase = str(input('Qual seu nome completo: '))
print('Seu nome em letras maiúsculas é '.format(frase.upper()))
print('Seu nome em letras minúsculas é '.format(frase.lower()))
print('O seu nome têm {} letras'.format(len(frase)-frase.count(' ')))
primeiroNome = frase.split()
print('O seu primeiro nome é {} que tem {} letras'.format(primeiroNome[0], len(primeiroNome[0])))
"""
poderia ter feito essa de achar o primeiro nome com find(' '), aqui ele estaria procurando a primeira posição"""
