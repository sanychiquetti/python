# Crie um programa que leia quanto a pessoa tem de dinheiro na carteira, e mostre
# quantos dólares ela pode comprar
# considere: US$ 1,00 = RS$ 3,27
reais = float(input('How many reais do you have in your wallet? R$ '))
dollars = reais / 3.27
print('You can buy US$ {:.2f} dollars with R$ {:.2f}'.format(dollars, reais))

