# Classificando atletas conforme a idade. 

ano = int (input('Ano de nascimento: '))
atual = 2023
idade = atual - ano

if idade <= 9:
    print('Você tem {} e está na categoria MIRIM. ' .format(idade))
    
elif idade <= 14:
    print('Você tem {} e está na categoria INFANTIL. ' .format(idade))

elif idade <= 19:
    print('Você tem {} e está na categoria JUNIOR. ' .format(idade))
    
elif idade <= 25:
    print('Você tem {} e está na categoria SÊNIOR.' .format(idade))
    
else: 
    print('Você tem {} e está na categoria MASTER.' .format(idade))     