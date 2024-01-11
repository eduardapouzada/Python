# Perguntar o valor da casa, o salario, e em quantos anos vai pagar. 
# Calcular prestação mensal, sabendo que ela não pode passar de 30% do salario 
# ou então o salario sera negado.

casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário: '))
anos = int (input('Informe quantos anos de financiamento: '))

mensal = casa / (anos * 12)

x = salario * 0.30

if mensal <= x:
    print('Empréstimo aceito. A prestação mensal será de R${:.2f}' .format(mensal))
    
else:
    print('Empréstimo negado.')    
    