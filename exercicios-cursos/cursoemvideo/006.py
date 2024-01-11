#Crie um algoritmo que leia um número e mmostre seu dobro, seu
# triplo e sua raiz quadrada.

num = int(input('Digite um número inteiro: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)


print('O dobro de {} é {} ' .format(num, dobro))
print('O triplo de {} é {}' .format(num, triplo))
print('A raiz de {} é {:.2f}' .format(num, raiz)) 