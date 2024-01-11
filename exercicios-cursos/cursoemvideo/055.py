# Ler o peso de cinco pessoas e no final mostrar qual o maior e menor peso;

maior = 0
menor = 0

for pessoas in range(1,6):
    peso = float(input(f'Digite o peso da {pessoas}º pessoa: '))
    if pessoas == 1: # PARA SABER SE É A PRIMEIRA VEZ SENDO RODADO, SE FOR, O PESO INICIAL É O MAIOR E MENOR
        maior = peso
        menor = peso
    else: # DEPOIS DA PRIMEIRA RODADA, SEMPRE VIRÁ PRA CA
        if peso > maior:
            maior = peso # MAIOR RECEBENDO O PESO MAIOR

        if menor > peso:
                menor = peso # MENOR RECEBENDO O PESO MENOR

print(f'O maior peso é {maior}')
print(f'E o menor peso é {menor}')
