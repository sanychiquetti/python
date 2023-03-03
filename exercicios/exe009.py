# Faça um programa que leia um número inteiro e mostre sua tabuada.
table = int(input('What number do you want the multiplication table: '))
"""one = table * 1
two = table * 2
three = table * 3
four = table * 4
five = table * 5
six = table * 6
seven = table * 7
eight = table * 8
nine = table * 9
ten = table * 10
print('The multiplication table of {} is: \n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}'.format(table, one, two, three, four, five, six, seven, eight, nine, ten))
"""
print('\n')
for i in range (1,11):
    r = i * table
    print('{} * {} = {}'.format(table, i, r))
    i = i + 1

