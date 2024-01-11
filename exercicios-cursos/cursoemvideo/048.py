# Calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 a 500.
i = 0
for a in range (0, 500, 3):
    if a % 2 != 0:
        i = i + a 
print('A soma de todos os números ímpares entre 1 e 500, que são multiplos de 3 são: {}' .format(i))
    