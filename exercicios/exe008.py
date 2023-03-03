# Escreva um programa que leia um valor em metros, e o exiba convertido em centímetros e milímetros
meters = float(input('Enter the meters '))
centimeter = meters * 100
millimeter = meters * 1000
print('The {} meters is {} centimeters and {} millimeters'.format(meters, centimeter, millimeter))
