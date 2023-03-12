nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi de {} '.format(media))
if media >= 6.0:
    print('Sua médida foi boa! Parabéns!')
else:
    print('Sua média foi baixa" Precisa estudar mais!')
