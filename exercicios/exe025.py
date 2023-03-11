"""Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva'
no nome."""
nome = str(input('Qual seu nome? ')).strip() #tiro os espaço da frente, se ele tiver...
print('No seu nome tem Silva? {}'.format('silva' in nome.lower()))
