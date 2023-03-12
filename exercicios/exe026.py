"""
Faça um programa que leia uma frase e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
"""

frase = input('Digite uma frase que você mais gosta: ').upper().strip()
print('A letra A aparece {} vezes na sua frase'.format(frase.count('A')))
print('Ela aparace pela primeira vez na posição {}'.format(frase.find('A')+1)) # colocar + 1, pois inicia com 0, assim fica mais legível
print('Ela aparace pela última vez na posição {}'.format(frase.rfind('A')+1)) #com o r, ele procura da direita pra esquerda