# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com
# 5% de desconto.
shoesPrice = float(input('How much are these shoes? '))
discount = (shoesPrice * 5) / 100
newPrice = shoesPrice - discount
print('The value of discounted shoes is R$ {:.2f}'.format(newPrice))
