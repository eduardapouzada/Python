"""
 leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
 e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
 continuar a digitar valores.
"""

num = int(input('Digite um número: '))
opção = str(input('Deseja continuar digitando números?')).lower()
cont = 0
media = 0
soma = 0
while opção == 'sim':

    num = int(input('Digite um número: '))
    opção = str(input('Deseja continuar digitando números?')).lower()
    soma += num
    cont += 1
media = soma/cont
print(f'Você digitou {cont} números e a media deles é {media}')

