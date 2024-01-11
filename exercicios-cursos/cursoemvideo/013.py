# Leia um salario e mostre um novo salario com 15% de desconto.

salario = float(input('Digite seu salario: '))

desconto = salario * 0.15
novo = salario + desconto

print('O novo salario com 15% de aumento é {:.2f}' .format(novo))