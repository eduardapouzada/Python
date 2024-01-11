#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto.

preço = float(input('Digite o preço: '))

desc = preço * 0.05
novo = preço - desc

print('O novo preço é: {:.2f}' .format(novo))