"""  
Crie uma função recursiva que escreva na tela o número entregue por parâmetro e
seus sucessivos divisores por 2 (divisão inteira), até que o número seja menor que 1. A
função deve escrever de forma invertida
"""

def divisores_por_2_invertido(numero):
    if numero < 1:
        return
    divisores_por_2_invertido(numero // 2)
    print(numero)

divisores_por_2_invertido(100)
