""" 
Faça um programa em Python que leia um arquivo texto, e mostre na tela o total de
vogais, o total de consoantes e o total de caracteres que não são nem vogais e nem
consoantes contidos neste arquivo.
"""

with open('aed-3bi/2lista/arquivodois.txt', 'r') as arquivo:
    cont_vogais = 0 
    cont_conso = 0
    cont = 0

    for linha in arquivo:
        for caracter in linha:

            if caracter.isalpha():
                if caracter.lower() in 'aeiou':
                    cont_vogais += 1

                if caracter.lower() in 'bcdfghjklmnpqrstvwxyz':
                    cont_conso += 1
            else:
                cont += 1

print(f'Este arquivo contem {cont_vogais} vogais; {cont_conso} consoantes e {cont} caracteres que não são nem vogais e nem consoantes.')    