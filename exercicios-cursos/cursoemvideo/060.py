# Faça um programa que leia um número qualquer e mostre o seu fatorial

num = int(input('Qual numero deseja fatorar? '))
c = num
resul = 1
while c > 0:
    print(c, end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    resul = resul * c
    c = c - 1


print(f'{resul}')
