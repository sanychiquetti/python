"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
"""
num = int(input('Digite um número: '))
num = num %2 == 0
if num ==0:
    print('Esse número é ímpar')
else:
    print('Esse número é par')