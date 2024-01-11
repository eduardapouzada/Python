# Pedra, papel e tesoura.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções:
      [ 0 ] PEDRA 
      [ 1 ] PAPEL 
      [ 2 ] TESOURA''')

jogador = int(input('Qual sua jogada? '))

print('-=' * 12)

print('O computador jogou {}' .format(itens[computador]))
print('O jogador jogou {}' .format(itens[jogador]))

print('-=' * 12)

if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
        
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2: 
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
        
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
        
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2: 
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
        
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
        
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2: 
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')        
            