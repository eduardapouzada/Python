# Calcule IMC 

peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / (altura**2)

if imc <= 18.5:
    print('Seu IMC é {:.1f}. Abaixo do peso.' .format(imc))
    
elif imc <= 25:
    print('Seu IMC é {:.1f}. Peso ideal.' .format(imc))
    
elif imc <= 30:
    print('Seu IMC é {:.1f}. Sobrepeso.' .format(imc))

elif imc <= 40:
    print('Seu IMC é {:.1f}. Obsidade.' .format(imc))

else:
    print('Seu IMC é {:.1f}. Obesidade Mórbida.' .format(imc))        
    