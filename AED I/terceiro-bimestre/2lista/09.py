"""  
 Escreva um programa, em Python, que leia dois nomes de arquivos. Após informado os
nomes, o programa deverá copiar o conteúdo do arquivo fonte (o primeiro) para o arquivo
destino (o segundo). Deve verificar se os arquivos existem. Se o arquivo destino existir, as
informações do arquivo fonte devem ser acrescentadas ao arquivo destino. Considere que o
conteúdo do arquivo fonte é um texto. Seu programa não deve copiar linhas comentadas
(que comecem com //).
"""
import os

um = str(input('Nome do primeiro arquivo: '))
dois = str(input('Nome do segundo arquivo: '))
nomeUM = 'aed-3bi/2lista/' + um +'.txt'
nomeDOIS = 'aed-3bi/2lista/' + dois + '.txt'

def verificar(arquivoUM, arquivoDOIS):
    if os.path.exists(arquivoUM):
        if os.path.exists(arquivoDOIS):
            with open(arquivoUM, 'r', encoding='utf-8') as arquivo_fonte:
                with open(arquivoDOIS, 'r+', encoding='utf-8') as arquivo_destino:
                    for linhas in arquivo_fonte: 
                        if not linhas.startswith('//'):
                            arquivo_destino.write(linhas) 
                            
                        
    else:
        print('ERRO')                    
                    
               
verificar(nomeUM, nomeDOIS)                
                
                
        