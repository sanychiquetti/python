"""
Dsenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km rodado para viagens até 200KM
e R$ 0,45 para viagens mais longas.
"""
km = float(input('Qual a distância em km até a sua cidade? '))
if km >=200:
    print('O valor da passagem será de R$ {:.2f}'.format(km * 0.5))
else:
    print('O valor da sua passagem será de R$ {:.2f}'.format(km * 0.45))
print('Boa Viagem!')