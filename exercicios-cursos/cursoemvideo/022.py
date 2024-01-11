# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome em maiuscula
#O nome em minuscula
# Quantidade de letras 
# Mostra o primeiro nome e quantas letras tem.

nome = str(input('Digite seu nome completo: ')).strip() #strip para eliminar espaços.

print('Seu nome em maiusculo: {}.' .format(nome.upper()))
print('Seu nome em minuscula: {}. ' .format(nome.lower())) 
print('Quantidade de letras do seu nome: {}.' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.' .format(nome.find(' ')))
 