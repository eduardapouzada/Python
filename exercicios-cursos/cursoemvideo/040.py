# Calcular a média.

nota1 = float(input('Sua primeira nota: '))
nota2 = float(input('Sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média é {:.1f}. Você está reprovado.' .format(media))
    
elif media >= 5.0 and media <= 6.9:
    print('Sua média é {:.1f}. Você está de recuperação.' .format(media))    

else:
    print('Sua média é {:.1f}. Você está aprovado.' .format(media)) 