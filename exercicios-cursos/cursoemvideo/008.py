#Escreva um programa que leia um valor em metros e o 
# exiba convertido em centimetros e milimetros.

m = float(input('Digite um valor em metros: '))

cm = m * 100
mm = m * 1000

print('{} em centimetros é {:.0f}cm e em milimetros é {:.0f}mm' .format(m, cm, mm))