"""
Faça um programa em Python que leia um arquivo texto, e mostre na tela quantas linhas
esse arquivo possui.
"""

with open ('aed-3bi/2lista/arquivoum.txt', 'r') as arquivo:
        
    cont = 0
    for linha in arquivo:
        cont += 1
        
print(f'O arquivo tem {cont} linhas.')   
