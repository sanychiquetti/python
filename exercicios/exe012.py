# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com
# 5% de desconto.
shoesPrice = float(input('How much are these shoes? R$ '))
newPrice = shoesPrice - (shoesPrice * 5 / 100)
print('The shoes that costs R$ {:.2f}, with the discount now the shoes cost R$ {:.2f}'.format(shoesPrice, newPrice))
