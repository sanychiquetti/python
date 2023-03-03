# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a sua raiz quadrada.
numInf = int(input('Digite um número, e vou te mostrar o seu dobro,seu triplo e sua raiz quadrada: '))
dobro = numInf * 2
triplo = numInf * 3
raizQ = float(numInf) ** (1/2)
print('O dobro de {} é {}, \n seu triplo é {} \n e a sua raiz quadrada é {:.3f}'.format(numInf, dobro, triplo, raizQ))
