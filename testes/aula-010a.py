# Aula de se e senao - estrutura condicional
"""tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')
print('--FIM--')"""

# outra forma de fazer mais simplificada:
tempo = int(input('Quantos anos tem seu carro? '))
print('Seu carro é novo' if tempo<=3 else 'Seu carro é velho')
print('--FIM--')
