#Faça um programa que leia um número inteiro e moste na tela
# o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1

print('O sucessor do número {0} é {1} e seu antecessor é {2}' .format(num, sucessor, antecessor))