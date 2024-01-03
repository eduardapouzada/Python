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
usu = str(input('Digite um comentário: ')) 
def menção(usuario):
    if '@' in usuario:
        print(f'Este comentário possui uma menção a um usuário.')
        
        
    else:
        print('Este comentário não possui menção a um usuário.')
       
       

menção(usu)       