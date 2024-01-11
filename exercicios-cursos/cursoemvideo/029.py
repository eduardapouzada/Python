# Escreva um programa que leia a velocidade de um carro. 
# Se ela ultrapassar 80km, mostreuma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7 por cada km acima do limite. 

carro = float(input('Digite a velocidade do carro: '))

if carro > 80:
    multa = (carro - 80) * 7 
    print('Você ultrapassou o limite. E recebeu uma multa de R${}' .format(multa))
    
else:
    print('Você não ultrapasssou o limite. E não recebeu uma multa.')    