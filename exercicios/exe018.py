"""
Faça um programa que leia um ângulo qualquer e mostre na tela o seno,
 cosseno e a tangente desse ângulo.
"""
import math
ag = float(input('Digite o ângulo que você quer ver: '))
seno = math.sin(math.radians(ag)) #estou pegando o radiano do ângulo e convertendo em seno
print('O seno de {} é {:.2f}'.format(ag, seno))
cos = math.cos(math.radians(ag))
print('O cosseno de {} é {:.2f}'.format(ag, cos))
tag = math.tan(math.radians(ag))
print('A tangente de {} é {:.2f}'.format(ag, tag))