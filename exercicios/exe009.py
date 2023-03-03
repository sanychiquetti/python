# Faça um programa que leia um número inteiro e mostre sua tabuada.
table = int(input('What number do you want the multiplication table: '))
print('_' * 12)
print('{} * {:2} = {}'.format(table, 1, table*1))
print('{} * {:2} = {}'.format(table, 2, table*2))
print('{} * {:2} = {}'.format(table, 3, table*3))
print('{} * {:2} = {}'.format(table, 4, table*4))
print('{} * {:2} = {}'.format(table, 5, table*5))
print('{} * {:2} = {}'.format(table, 6, table*6))
print('{} * {:2} = {}'.format(table, 7, table*7))
print('{} * {:2} = {}'.format(table, 8, table*8))
print('{} * {:2} = {}'.format(table, 9, table*9))
print('{} * {:2} = {}'.format(table, 10, table*10))
print('_' * 12)

""" forma avançada de fazer:
print('\n')
for i in range (1,11):
    r = i * table
    print('{} * {} = {}'.format(table, i, r))
    i = i + 1
"""

