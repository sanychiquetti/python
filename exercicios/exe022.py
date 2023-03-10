"""
Crie um programa que leia um nome completo de uma pessoa e mostre:
O nome com todos as letras maiúsculas
O nome com todos as letras minúsculas
Quantas letras ao todo sem os espaços
Quantas letras tem o primeiro nome
"""
frase = input('Qual seu nome completo: ')
print(frase.upper())
print(frase.lower())
spaces = (frase.count(" "))
compr = len(frase) - spaces
print('O seu nome têm {} letras'.format(compr))
primeiroNome = frase.split()
print('O seu primeiro nome é {} que tem {} letras'.format(primeiroNome[0], len(primeiroNome[0])))
