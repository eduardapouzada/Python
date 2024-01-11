""" Faça um programa que leia vários números até o usuario digitar
999, e então mostre quantos números foram digitados e a soma entre eles.
(desconsiderando o flag)
"""

cont = 0
soma = 0
while True:
    num = int(input('Digite um número[999 para parar]: '))
    if num != 999:
        cont +=1
        soma += num
    else:
        break
print(f'Você digitou {cont} números. E a soma entre eles é {soma}.')