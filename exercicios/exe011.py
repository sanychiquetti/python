# Faça um programa que leia a largura e a altura em metros de uma parede, calcule
# a área e a qdade de tinta necessária para pintá-la, sendo que cada litro de tinta,
# pinta uma área de 2 metros quadrados.
withWall = float(input('How wide is your wall: '))
heightWall = float(input('What is de height of your wall? '))
squareMeters = (withWall * heightWall) / 2
print('Your wall have {:.2f} meters \nAnd you will need {:.2f} liters of paint'.format((withWall*heightWall), squareMeters))
