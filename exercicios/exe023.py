"""
Faça um programa que leia um número de 0 até 9999 e mostre
na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
num = (input('Digite um número de 0 até 9999: '))
print('A unidade do número {} é {}'.format(num, (num[3])))
print('A dezena do número {} é {}'.format(num, (num[2])))
print('A centena do número {} é {}'.format(num, (num[1])))
print('A milhar do número {} é {}'.format(num, (num[0])))
"""
forma de fazer com matemática:
num = (input('Digite um número de 0 até 9999: '))
und = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10 
print ('unidade é = {}'.format(und))
print ('dezena é = {}'.format(dez))
print ('centena é = {}'.format(cent))
print ('milhar é = {}'.format(mil))
"""