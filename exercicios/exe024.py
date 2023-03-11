"""
Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "Santo".
"""

city = str(input('Qual o nome da sua cidade? ')).strip() #elimino os espaços se, o usuário deu espaços antes no teclado
print(city[:5].lower() == 'santo') #conto qtas letras tem santo acrescento mais uma, e comparo se ela é igual a escrita no teclado
