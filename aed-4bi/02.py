"""  
Um sistema de LOG armazena em um arquivo os logins dos usuários que
acessaram o site, da seguinte forma (tabela à esquerda):
No entanto, o usuário deseja uma versão resumida, que apresenta o login de um
usuário e o número de vezes que o login apareceu, conforme exemplo à direita. Crie
um programa que leia um arquivo de LOG como apresentado no original e escreva
um arquivo CSV no formato da versão resumida.
"""

with open('aed-4bi/log.txt', 'r', encoding='utf-8') as arquivo:
    lido = arquivo.readline()
    
    cont = 0
    for linhas in lido:
        print(linhas[cont])
        cont += 1
        
        