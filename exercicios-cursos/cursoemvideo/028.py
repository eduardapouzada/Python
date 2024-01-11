# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuario ganhou ou perdeu. 

import random 

x = random.randint(0, 5)

n = int(input('Chute o número entre 0 e 5: '))

if n == x:
    print('O número é o {}. Você venceu!!!' .format(x))

else: 
    print('O número era {}. O computador venceu!!!' .format(x))    