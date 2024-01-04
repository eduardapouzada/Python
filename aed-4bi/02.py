"""  
Um sistema de LOG armazena em um arquivo os logins dos usuários que
acessaram o site, da seguinte forma (tabela à esquerda):
No entanto, o usuário deseja uma versão resumida, que apresenta o login de um
usuário e o número de vezes que o login apareceu, conforme exemplo à direita. Crie
um programa que leia um arquivo de LOG como apresentado no original e escreva
um arquivo CSV no formato da versão resumida.
"""

dic = {}
with open('aed-4bi/log.txt', 'r', encoding='utf-8') as arquivo:
    lido = arquivo.readlines()
    
    for linha in lido:       
        linha = linha.strip()    
        if linha in dic:
            dic[linha.strip()] += 1

        else:
            dic[linha.strip()] = 1
    print(dic)            
    

with open('aed-4bi/arquivo.csv', 'w', encoding='utf-8') as novoarquivo:
    
    for chave in dic:
        valor = dic[chave]
        novoarquivo.write(f"{chave}, {valor}\n")   
    print('novo arquivo criado com sucesso.')    
    