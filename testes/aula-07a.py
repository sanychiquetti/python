"""
posso colocar o return com espaços definidos(aqui estou pedindo 20 espaços:
nome = input('What´s your name? ')
print('Nice too meet you {:20}!'.format(nome))
"""

"""
posso colocar o return com espaços definidos e colocar centralizando:
nome = input('What´s your name? ')
print('Nice too meet you {:^20}!'.format(nome))
"""

"""
posso colocar o return com espaços definidos, centralizando e com =
nome = input('What´s your name? ')
print('Nice too meet you {:=^20}!'.format(nome))
"""

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
soma = numero1 + numero2
multi = numero1 * numero2
divisao = numero1 / numero2 #posso delimita as casas decimais: :.3f - lá no {}
divisaoInteira = numero1 // numero2
restoDivisao = numero1 % numero2
exponenciacao = numero1 ** numero2

"""
#para colocar tudo na mesma linha, mesmo tendo 2 print´s, coloco end=' '
print('A soma vale {}, seu produto vale {}, e a divisao é {:.3f}, sua exponenciação é {}' .format(soma, multi, divisao, exponenciacao), end=' ')
print('E a sua divisão inteira deu {} e o resto da divisão ficou em {}'.format(divisaoInteira, restoDivisao))-
"""

#Agora se quero quebrar a linha que está no mesmo comando posso colocar \n, evitamos, colocar vários print
print('A soma vale {}, \n seu produto vale {}, \n e a divisao é {:.3f},\n sua exponenciação é {}' .format(soma, multi, divisao, exponenciacao))
print('E a sua divisão inteira deu {} e o resto da divisão ficou em {}'.format(divisaoInteira, restoDivisao))
