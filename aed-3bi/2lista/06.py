"""  
Escreva um programa que leia um arquivo, gerando um novo arquivo com o mesmo
conteúdo, porém com todas as vogais convertidas para maiúsculas. Os nomes dos arquivos
serão fornecidos, via teclado, pelo usuário.

"""
um = str(input('PRIMEIRO ARQUIVO: '))
dois = str(input('SEGUNDO ARQUIVO: '))

def arquivos(nomeUM, nomeDOIS):
    nome = 'aed-3bi/2lista/' + nomeUM
    nome2 = 'aed-3bi/2lista/' + nomeDOIS   
    
    with open(nome, 'w') as arquivoUM:
        conteudo = 'Python e uma linguagem de programacao de alto nivel, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinamica e forte.'
        arquivoUM.write(conteudo.lower())
        
    with open(nome, 'r+') as arquivoUM:
        with open(nome2, 'w') as arquivoDOIS:
            for caracter in arquivoUM.read():
                if caracter in 'aeiou':
                    arquivoDOIS.write(caracter.upper())
                else:
                    arquivoDOIS.write(caracter)    
       
arquivos(um, dois)        
        