"""aqui vamos importar apenas as bibliotecas de matemática que vamos usar:
import random
from math import sqrt,floor
num = int(input('Digite um número: '))
raiz = sqrt(num) #veja que não preciso mais colocar o math antes..
print('A raiz quadrada de {} é {:.2f}'.format(num, floor(raiz)))
"""
#se eu quiser importar a função random, que faz números aleatórios:
import random
num = random.randint(2,10) #com o randint estou colocando que quero só numeros inteiros e que sejam entre 2 e 10
print(num)

