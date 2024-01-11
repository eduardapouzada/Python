# Calcula o preço da passagem. R$0,50 por 200km. E R$0,45 para viagens mais longas.

d = float(input('Digite a distância da viagem para calcular a passagem: '))

a = d * 0.50
b = d * 0.45

if d <= 200:
    print('A distância é {}km e o valor da passagem é R${:.2f}. ' .format(d, a)) 
    
    
else:
    print('A distância é {}km e o valor da passagem é R${:.2f}. ' .format(d, b))    
    