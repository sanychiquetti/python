# Faça um programa que leia a largura e a altura em metros de uma parede, calcule
# a área e a qdade de tinta necessária para pintá-la, sendo que cada litro de tinta,
# pinta uma área de 2 metros quadrados.
withWall = int(input('Wow wide is your wall '))
heightWall = int(input('What is de height of your wall? '))
squareMeters = (withWall * heightWall) / 2
print('You will need {} liters of paint'.format(squareMeters))
