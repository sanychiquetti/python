"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por km acima do limite.
"""
veloz = float(int(input('Qual a velocidade do carro? ')))
velozMaxima = 80
multa = (veloz - 80) * 7.00
if veloz > 80:
    print('Você está acima da velocidade máxima que é {}km'.format(velozMaxima))
    print('A multa vai custar R$ {:.2f}'.format(multa))
print('Parabéns você não ultrapassou a velocidade máxima, que é {}km'.format(velozMaxima))