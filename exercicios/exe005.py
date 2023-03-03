# Faça um programa que leia um número inteiro, e mostre na tela o seu sucessor e o antecessor:
numInt = int(input('Digite um número: '))
antecessor = numInt - 1
sucessor = numInt + 1
print('O antecessor do número {} é o número {}, e o sucessor dele é o número {}'.format(numInt, antecessor, sucessor))