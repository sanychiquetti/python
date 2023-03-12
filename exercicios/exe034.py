"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor
do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para salários inferiores ou igual, o aumento é de 15%.
"""
salario = float(input('Qual seu salário? R$ '))
if salario <= 1250:
    print('Seu salário será R$ {:.2f} com o aumento de 15%'.format((salario * 15/100) + salario))
else:
    print('Seu novo salário será de R$ {:.2f} com o aumento de 10%'.format((salario * 10/100) + salario))