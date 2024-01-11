# Fazer uma lista com cinco elementos e mostrar qual o maior e menos e suas posições.

lista = []
maior = 0
menor = 0
p = 0

for l in range(0,5):
    lista.append(int(input('Digite um número para a posição {}: ' .format(l))))

    if lista[l] > maior:
        maior = lista[l]
        p == lista[l]

    else:
        if lista[l] > menor and lista[l] < maior:
            menor = lista[l]
        
print('Sua lista completa é {}.\n E na posição {} está seu maior numero, o {}. ' .format(lista, p, maior)) 