"""  
Você deve criar um jogo de dados em Python onde o jogador lança dois
dados de seis faces e tenta adivinhar se a soma dos números nos dados será maior
ou igual a um determinado valor escolhido. Implemente uma função chamada
lançar_dados, que simula o lançamento de dois dados de seis faces (sortear) e
retorna a soma dos resultados. Implemente uma função chamada validar_aposta,
que verifica se a aposta do jogador é um número inteiro positivo entre 2 e 12.
Exemplo:
Bem-vindo ao Jogo de Dados!
Digite o valor alvo (2-12): 7
Lançando os dados...
Os números nos dados somam 8.
Você ganhou a aposta! A soma dos dados é maior ou igual a 7
"""
import random
def lançar_dados():
    sorteado1 = random.randint(1, 6)
    sorteado2 = random.randint(1, 6)
    soma = sorteado1 + sorteado2

    def validar_aposta(aposta):
        if aposta >= 2 and aposta <= 12:
            if aposta < soma:
                print(f'Você ganhou a aposta! A soma dos dados é maior ou igual a {aposta}')
            else:
                print(f'Você perdeu a aposta! A soma dos dados é menor que {aposta}')
        
        else:
            print(f'{aposta} é um valor inválido. Sua aposta deve ser um valor inteiro.')


    num = int(input('Bem vindo ao jogo de dados!!! \nDigite o valor alvo (2-12): '))            
            
    validar_aposta(num)    
    
    
        
lançar_dados()
    