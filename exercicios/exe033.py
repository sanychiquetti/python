"""
Faça um programa que leia 3 números, e moste qual é o número
 maior e qual é o menor.
"""
lista = (input('Digite 3 números: '))
lista = sorted(lista)
print('O maior número digitado é {}'.format(lista[len(lista)-1]))
print('O menor número digitado é {}'.format(lista[0]))
