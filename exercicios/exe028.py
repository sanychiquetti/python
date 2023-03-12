"""
Escreva um programa que faça o computador "pensar" em um número inteiro, entre 0
e 5, e peça para o usuário tentar descobrir qual foi o número pensado pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
print('-*=*-' * 8)
print('        Vamos jogar advinhação? ')
print('-*=*-' * 8)
chute = int(input('Pensei em um número de 0 a 5, qual número pensei? '))
sorteio = random.randint(0, 6)
if chute == sorteio:
    print('Você acertou! O número que pensei foi {}'.format(sorteio))
else:
    print('Você errou! O número que pensei foi {}'.format(sorteio))

