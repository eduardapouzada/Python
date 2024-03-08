"""  
 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
 mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

sorteados = (randint(1,10), randint(1,10), randint(1,10), randint(1,10))


print(f'Os números sorteados: ', end='')

for i in sorteados:
    print(f'{i}', end=' ')

print(f'\nO maior número sorteado: {max(sorteados)} \nO menor número sorteado: {min(sorteados)} ')

"""

maior = 1
menor = 1

for i in sorteados:
    print(f'{i}', end=' ')
    if  i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'\nO maior número sorteado: {maior} \nO menor número sorteado: {menor} ')
"""