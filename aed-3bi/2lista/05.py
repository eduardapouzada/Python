"""   
Faça um programa que leia um arquivo texto. Crie outro arquivo texto contendo o texto
do arquivo de entrada, mas com as vogais substituídas por um * (asterisco).

"""

with open('aed-3bi/2lista/arquivodois.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

with open('aed-3bi/2lista/arquivoCriado.txt', 'r+', encoding='utf-8') as arquivoCriado:
    for caracter in conteudo.lower():
        if caracter in 'aeiou':
            arquivoCriado.write('*')
        else:
            arquivoCriado.write(caracter)
