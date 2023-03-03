# Faça um algoritmo que leia o salário de um funcionário, e mostre o novo valor com 15%
# de aumento.
wage = float(input('How much do you earn? '))
newWage = (wage * 15) / 100 + wage
print('Your new wage is R$ {:.2f}'.format(newWage))