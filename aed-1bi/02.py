""" 
Crie um programa em Python que imprima uma sequência de números
em forma de pirâmide. O programa deve solicitar ao usuário um número inteiro
positivo e, em seguida, imprimir os números de 1 até o número informado, em linhas
crescentes e decrescentes, formando uma pirâmide.
Exemplo:
Digite um número inteiro positivo: 4

1
12
123
1234
4321
321
21
1
"""

num = int(input('Digite um número inteiro positivo para formar a pirâmide: '))

def piramide(numero):
    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    for i in range(numero, 0, -1):
        for j in range(i, 0, -1):  
            print(j, end="")
        print() 
piramide(num)    