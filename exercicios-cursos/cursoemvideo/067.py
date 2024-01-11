"""Faça o programa mostrar a tabuada que o usuario quiser.
O programa sera interrompido quando o usuario digitar um número negativo
"""

while True:
    num = int(input('Qual tabuada? '))
    if num > 0:
        for n in range(0,11):
            mult = num * n
            print(f'{num} x {n} = {mult}')

    else:
        break
print('Você digitou número negativo e saiu do programa!!')