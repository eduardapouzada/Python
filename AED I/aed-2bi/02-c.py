""" 
O Instagram é uma popular plataforma de mídia social que permite aos
usuários compartilhar fotos e vídeos. Considere um cenário em que você está
desenvolvendo uma funcionalidade para analisar os comentários em postagens do
Instagram.
a) Escreva um código em Python que verifique se uma string comentário contém a
menção a um usuário. Uma menção começa com o símbolo "@" seguido por um
nome de usuário válido (composto apenas por letras minúsculas e números), por
exemplo: "@usuario123".
b) Escreva um código em Python que substitua todas as menções a usuários na string
comentário por "USUARIO_MENCIONADO".
c) Dado um conjunto de palavras proibidas, escreva um código em Python que
verifique se a string comentário contém alguma das palavras proibidas. Se contiver,
exiba "Conteúdo inadequado", caso contrário, exiba "Comentário permitido"
"""

proibidas = ['pqp', 'vsf']

comentario = str(input('Digite um comentário: (Este comentário passsara por verificação.) '))

def verifica(palavras):
    palavras = palavras.split() 
    for palavra in palavras:
        if palavra.lower() in proibidas:
            print('Conteúdo inadequado')
            return  
    print('Comentário permitido')  
 
verifica(comentario)        