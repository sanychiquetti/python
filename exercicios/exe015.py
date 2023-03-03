#Escreva um programa que pergunte a qdade de Km percorridos, por um carro alugado, e a qdade de dias
#que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0.15
# por Km rodado.
diasAlugado = int(input('Quantos dias de aluguel? '))
KmRodado = float(input('Quantos km foram rodados? '))
custoTotal = (diasAlugado * 60) + (KmRodado * 0.15)
print('O valor total do aluguel por {} dias e {} km rodados é de R$ {:.2f}'.format(diasAlugado, KmRodado, custoTotal))