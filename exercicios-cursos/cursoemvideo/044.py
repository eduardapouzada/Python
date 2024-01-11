# Calcule o valor a ser pago pelo produto.

preço = float(input('Qual o preço? R$'))
print('Formas de pagamento \n[ 1 ] à vista dinheiro/cheque \n[ 2 ] á vista no cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual a opção? '))

if opção == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preço,   preço - (preço * 0.10)))
    
elif opção == 2:
    print( 'Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preço, preço - (preço * 0.05) ))
    
elif opção == 3:
    print( 'Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preço, preço))    
    
elif opção == 4:
    print( 'Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preço, preço + (preço * 0.20)))
    
else:
    print('Opção Inválida.')    