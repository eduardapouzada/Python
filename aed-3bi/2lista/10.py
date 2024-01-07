"""  
Faça um programa, em Python, que leia os nomes de um arquivo de entrada e outro de
saída. O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes na sequência (não há delimitador entre os
conteúdos). O programa deverá ler o arquivo de entrada, e gerar um arquivo de saída onde
aparece o nome da cidade mais populosa, seguida pelo seu número de habitantes.
"""

entrada = str(input('Digite o nome do arquivo de entrada: '))
saida = str(input('Digite o nome do arquivo de saída: '))
nome_entrada = 'aed-3bi/2lista/' + entrada + '.txt'
nome_saida = 'aed-3bi/2lista/' + saida + '.txt'

def ler_Arquivos(arquivoEntrada, arquivoSaida):
    with open(arquivoEntrada, 'r+', encoding='utf-8') as arquivoE:
        lido = arquivoE.read()
        with open(arquivoSaida, 'w', encoding='utf-8') as arquivoS:
            