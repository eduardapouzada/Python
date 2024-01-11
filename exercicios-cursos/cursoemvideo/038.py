# Dois números inteiros. Dizer qual é o maior. 
# Dizer se não existe valor maior pois são iguais.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 == n2:
    print('Os valores são iguais.')
    
elif n1 > n2:
    print('O primeiro valor é maior. ') 
    
else:
    print('O segundo valor é maior.')       
    