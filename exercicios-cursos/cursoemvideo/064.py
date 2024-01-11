""" leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles """

n = int(input('Digite um número[999 para parar]: '))
cont = 0
soma = 0

while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite outro número[999 para parar]: '))

print(f'O total de números digitados foi {cont} e a soma entre eles é {soma}')