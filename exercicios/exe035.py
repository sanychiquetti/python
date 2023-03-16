"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
"""
ladoA = input('Digite o primeiro lado: ')
ladoB = input('Digite o segundo lado: ')
ladoC = input('Digite o terceiro lado: ')
if ladoA + ladoB <= ladoC or ladoB + ladoC <= ladoA:
    print('Não é um triângulo!')
else:
    print('É um triângulo!')
