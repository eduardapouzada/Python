# Três números e diga qual é maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('O número {} é o maior e o {} é o menor.' .format(n1, n3))
        
    else:
        print('O número {} é o maior e o {} é o menor.' .format(n1, n2))    
    
    
else: 
    if n2 > n1 and n2 > n3:
        if n1 > n3:
            print('O número {} é o maior e o {} é o menor.' .format(n2, n3))
        else:
            print('O número {} é o maior e o {} é o menor.' .format(n2, n1))
            
        
    else:
        if n1 > n2:
            print('O número {} é o maior e o {} é o menor.' .format(n3, n2))    
    
        else:
            print('O número {} é o maior e o {} é o menor.' .format(n3, n1))