""" Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção inteira.
"""
from math import ceil
num = input("Digite um número: ")
print("O número {} tem sua parte inteira {}".format(num, ceil(num)))
