"""
numero1 = input('Digite um valor: ')
print(type(numero1))
Veja que que mesmo que seja digitado um número,
ele vai retornar como str, precisa colocar o int antes para retornar um inteiro, veja abaixo:

numero1 = int(input('Digite um valor: '))
print(type(numero1))
aqui ele vai retornar como int, pois ele vai ler como números
"""

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
#print('A soma entre o número', numero1, 'e o numero', numero2, 'é dê:', soma)
# a forma mais fácil, e nova de fazer isso:
print('A soma entre o número {} e o número {} é de {}'.format(numero1, numero2, soma))
