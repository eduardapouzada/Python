from math import hypot
 
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

h = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}' .format(h))

# Leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
 