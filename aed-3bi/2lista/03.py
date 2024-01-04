"""  
Faça um programa em Python que leia um arquivo texto e um caractere. Mostre na tela
quantas vezes este caractere ocorre no arquivo.

"""

with open('aed-3bi/2lista/arquivodois.txt', 'r') as arquivo:
    cont = 0
    
    for linha in arquivo:
        for caracter in linha:
            if caracter.lower() in 'a':
                cont += 1
                
print(f'Esse arquivo de texto tem {cont} caracteres a.')    