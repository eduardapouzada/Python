#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos dolares ela pode comprar. Considere: Um dolar é 3,27 reais

real = float(input('Quanto dinheiro tem na sua carteira? R$'))

dolar = real / 3.27

print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))
 