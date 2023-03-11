"""
Faça um programa que leia uma frase e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
"""

frase = input('Digite uma frase que você mais gosta: ')
print('A letra A aparece {} vezes na sua frase'.format(frase.upper().count('A')))
print('Ela aparace pela primeira vez na posição {}'.format(frase.upper().find('A')))
