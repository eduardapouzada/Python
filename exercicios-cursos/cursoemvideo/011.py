# Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo
# que cada litro de tinta, pinta uma area de 2m.

largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura

tinta = area / 2

print('A quantidade necessaria para pintar a parede é: {}l' .format(tinta))