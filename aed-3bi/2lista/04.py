""" 
Faça um programa em Python que leia um arquivo texto e mostre na tela quantas vezes
cada letra do alfabeto aparece no arquivo.
"""

nome_arquivo = 'aed-3bi/2lista/arquivoum.txt'  # Substitua 'arquivo.txt' pelo nome do seu arquivo

# Inicializa um dicionário para armazenar a contagem de cada letra
contagem_letras = {letra: 0 for letra in 'abcdefghijklmnopqrstuvwxyz'}

# Abre o arquivo no modo de leitura
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        for caractere in linha.lower():  # Converte para minúsculas para contar independentemente de estar em maiúsculo ou minúsculo
            if caractere.isalpha():
                contagem_letras[caractere] += 1

# Exibe a contagem de cada letra
for letra, contagem in contagem_letras.items():
    
    print(f"A letra '{letra}' aparece {contagem} vezes no arquivo.")
