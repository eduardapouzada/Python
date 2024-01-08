"""  
 Desenvolva um sistema simples de gerenciamento de estoque para uma loja. Crie um programa
em Python que realiza as seguintes operações:
● Inicialização do Estoque:
● Crie um dicionário chamado estoque para armazenar informações sobre os
produtos em estoque.
● Cada chave do dicionário representa o nome de um produto, e o valor associado
é a quantidade disponível desse produto.
● Adição de Produtos:
● Crie uma função chamada adicionar_produto que aceite três parâmetros: o
dicionário de estoque, o nome do produto e a quantidade a ser adicionada.
● A função deve verificar se o produto já existe no estoque. Se existir, a quantidade
deve ser somada à quantidade existente. Se não existir, adicione o produto ao
estoque com a quantidade fornecida.
● Venda de Produtos:
● Crie uma função chamada vender_produto que aceite três parâmetros: o
dicionário de estoque, o nome do produto e a quantidade a ser vendida.
● A função deve verificar se o produto existe no estoque e se a quantidade a ser
vendida é menor ou igual à quantidade em estoque. Se for o caso, subtraia a
quantidade vendida do estoque. Caso contrário, imprima uma mensagem
informando que a venda não pode ser realizada por falta de estoque.
● Relatório de Estoque:
● Crie uma função chamada relatorio_estoque que aceite o dicionário de estoque
como parâmetro e imprima um relatório mostrando o nome de cada produto e sua
quantidade em estoque.
● Teste do Programa:
● Crie um código principal que inicialize o estoque, adicione alguns produtos, venda
alguns produtos e gere um relatório de estoque.

"""

dicionario = {'produto1': 5,
       'produto2': 8,
       'produto3': 4,
       'produto4': 7
}

print()
nome = str(input('Informe o nome do produto: '))
quant = int(input('Informe a quantidade: '))

def adicionar_produto(estoque, produto, quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade   
        
 
def vender_produto():
    
 
 
 
 
        
adicionar_produto(dicionario, nome, quant)   
print(dicionario)    


""" 
meu_dicionario = {'chave1': 'valor1', 'chave2': '4444', 'chave3': 'valor3'}

# Obtendo o valor associado à chave 'chave2'
valor_chave2 = meu_dicionario['chave2']

print(valor_chave2)  # Isso imprimirá 'valor2'
"""
