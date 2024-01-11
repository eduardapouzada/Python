# Três retas formam um triangulo. 
# Para isso, a soma de dois lados é menor que o terceiro lado.
# Dizer qual triangulo é;
# Equilatero: lados iguais
# Isosceles: um diferente
# Escaleno: todos diferentes.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As três retas podem formar um triângulo ' ,end='')
   
    if r1 == r2 == r3 != r1:
        print('equilatero')
   
    elif r1 != r2 != r3:
        print('escaleno') 
        
    else:
        print('Isosceles')     
    
else:
    print('As três retas não podem formar um triângulo.')   
    