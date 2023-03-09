"""
Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um trinângulo retângulo, calcule e mostre o comprimento da hipotenusa
ESSA É A FORMA MATEMATICA DE RESOLVER
op = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hipo = (op ** 2 + adj ** 2) ** (1/2)
print("A hipotenusa do triângulo é de {:.2f}".format(hipo))
"""

#aqui vamos fazer com o import hypotenusa da biblioteca:
from math import hypot
op = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(op, adj)
print("A hipotenusa do triângulo é de {:.2f}".format(hip))