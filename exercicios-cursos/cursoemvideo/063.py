""" Escreva um programa que leia um número N inteiro
qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
0  1    1    2
t1 t2  t3
   t1  t2
"""

num = int(input('Quantos termos você quer mostrar? '))
cont = 3
termo1 = 0
termo2= 1
termo3 = termo1 + termo2
print(f'{termo1} {termo2} {termo3}', end=' ')

while cont <= num:
    termo1 = termo2
    termo2= termo3
    termo3 = termo1 + termo2
    print(termo3, end=' ')
    cont += 1

print('FIM')