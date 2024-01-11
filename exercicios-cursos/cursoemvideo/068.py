"""
Um programa que jogue par ou impar com o computador.
O programa sera interrompido quando o jogador perder
e devera mostrar quantas vitorias consecutivas teve
"""

from random import randint

while True:
    jogador = str(input('Par ou impar? ')).lower()
    num_jogador = int(input('Informe o número: '))
    computador = randint(1,11)
    cont = 0
    tot = computador + num_jogador

    print(f'Você jogou {num_jogador} e o computador jogou {computador}, o total foi {tot}')

    if tot // 2 == 0:
        if jogador == 'par':
            print(f'Você ganhou!')
            cont += 1

    else:
        print(f'Você perdeu!')
    break


print(f'Você ganhou {cont} vezes seguidas')