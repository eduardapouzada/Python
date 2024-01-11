# Para salarios superiores a 1,250, aumento de 10% 
# Para inferiores, aumento de 15%

s = float(input('Digite seu salário: '))

a = 0.10
b = 0.15

if s >= 1250:
    aumento = s * a
    n = s + aumento
    print('Você recebeu um aumento de 10%. Seu salário agora é R${:.2f}' .format(n))
    
else:
    aumento = s * b
    n = s + aumento
    print('Você recebeu um aumento de 15%. Seu salário agora é R${:.2f}' .format(n))    
    
    