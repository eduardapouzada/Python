# Leia seis números inteiros, mostre a soma dos pares.

s = 0

for n in range (0, 6):    
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s = s + num
        
print('O resultado da soma dos números pares entre os seis números inteiros digitados é {}' .format(s))
   