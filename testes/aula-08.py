#aqui vamos importar a biblioteca toda de matemática:
import math
num = int(input('Digite um número: '))
#o math.sqrt é a função raiz quadrada
raiz = math.sqrt(num)
"""aqui estou usando a função arredondamento para cima com o math.ceil,
    se eu quizesse que ele apenas mostrasse 2 casas após a vírgula, era dentro do {}
    que eu deveria colocar :.2f
"""
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

