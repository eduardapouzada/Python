""" 
Crie um programa em Python que solicite ao usuário um número inteiro
positivo. O programa deve dividir esse número sucessivamente por 2 até que o
resultado seja menor que 1. Em cada divisão, o programa deve exibir o resultado da
divisão. Ao chegar a um resultado menor que 1, o programa deve exibir a mensagem
"Chegou a zero!".
Exemplo:
Digite um número inteiro positivo: 8
Resultado da divisão: 4.0
Resultado da divisão: 2.0
Resultado da divisão: 1.0
Chegou a zero
"""
numero = float(input('Digite um número para dividir: '))

def inteiros(num):
    
    while num > 1:
        num = num //2 
        print(f'Resultado da divisão: {num}')
        
    print('Chegou a zero!')    
    
inteiros(numero)    