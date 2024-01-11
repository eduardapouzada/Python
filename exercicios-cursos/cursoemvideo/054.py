# Ler sete data de nascimento e dizer quahntas pessoas ja tem 18;

cont = 0
conti= 0

for pessoas in range(1,8):
    ano = int(input(f'Qual ano a {pessoas} pessoa nasceu? '))
    if ano <= 2005:
        cont += 1


    else:
        conti += 1

print(f'{cont} pessoas maiores de idade.')
print(f'{conti} pessoas menores de idade.')