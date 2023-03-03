"""
Se eu quiser transformar o valor digitado em um número flutuante, posso escrever
antes do input, o float:
n = float(input('Digite um valor: '))
print(n)
digamos que o foi digitado 4, ele vai mostrar 4.0
"""

"""
Se colocarmos bool antes do input, ele vai trazer verdadeiro ou falso
n = bool(input('Digite um valor: '))
print(n)
#se digitarmos o 4, ele vai trazer verdadeiro, porque? Porque não demos parâmetro, então ele vai ler,
#tem um valor dentro? Tem, então é verdadeiro!
# se não digitarmos nada e dermos enter, então ele vai retornar falso, pois está vazio.
"""

#Assim como posso perguntar qual o tipo do dado inserido, tb posso perguntar qual se é numérico:
n = input('Digite algo: ')
print(n.isnumeric())
#Se digitar número ele vai dar true, se digitar texto vai dar false