""" 
 Considere um programa em Python que simula um jogo de cartas com um
baralho completo. O baralho é inicializado com 52 cartas, divididas em 4 naipes
(Paus, Ouros, Copas e Espadas) e 13 valores (de 2 a 10, Valete, Dama, Rei e Ás). O
programa deve utilizar listas para armazenar o baralho e sortear duas cartas para
cada um de 6 jogadores. Mostre na tela cada uma das cartas sorteadas para cada
jogador. Você não deve permitir que uma carta seja sorteada mais de uma vez.

"""
import random

naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']

baralho = []
for naipe in naipes:
    for valor in valores:
        carta = (valor, naipe)
        baralho.append(carta)
random.shuffle(baralho)

num_jogadores = 6

for jogador in range(1, num_jogadores + 1):
    print(f"Cartas do Jogador {jogador}:")
    cartas_jogador = []
    
    for _ in range(2):
        carta = baralho.pop()
        cartas_jogador.append(carta)
        print(f"  {carta[0]} de {carta[1]}")
    
    print() 
    
