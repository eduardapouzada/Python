"""  
Faça um programa que leia dois arquivos, e crie um terceiro arquivo com o conteúdo dos
dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo arquivo)
"""

with open('aed-3bi/2lista/primeiroArquivo.txt', 'r', encoding='utf-8') as arquivoUM:
    conteudoUM = arquivoUM.read()
    
with open('aed-3bi/2lista/segundoArquivo.txt', 'r', encoding='utf-8') as arquivoDOIS:
    conteudoDOIS = arquivoDOIS.read()
    
with open('aed-3bi/2lista/terceiroArquivo.txt', 'w', encoding='utf-8') as arquivoOFC:
        conteudoOFC = conteudoUM + '\n' + conteudoDOIS
        arquivoOFC.write(conteudoOFC)
        