# computador vai “pensar” em um número entre 0 e 10, e o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint

numero = randint(0, 10)
chute = 1
num = int(input('Pensei em um número de 0 a 10, tente adivinhar qual é: '))

while num != numero:
    num = int(input('Não é esse, tente novamente: '))
    chute += 1

print(f'Você acertou! Eu pensei no número {numero}, você chutou {chute} vezes.')
