# Faça um algoritmo que leia o salário de um funcionário, e mostre o novo valor com 15%
# de aumento.
wage = float(input('How much do you earn? R$ '))
newWage = (wage * 15) / 100 + wage
print('An employee who earned R${:.2f}, now your new wage is R$ {:.2f} with the 15% increase'.format(wage, newWage))