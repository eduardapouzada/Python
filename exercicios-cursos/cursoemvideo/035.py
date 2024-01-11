# Três retas formam um triangulo. 
# Para isso, a soma de dois lados é menor que o terceiro lado.

r1 = float(input('Digite o comprimento da reta um: '))
r2 = float(input('Digite o comprimento da reta dois: '))
r3 = float(input('Digite o comprimento da reta três: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As três retas podem formar um triângulo.')
    
else:
    print('As três retas não podem formar um triângulo.')   
    