# Palíndromo, lê de tras para frente, sem considerar os espaços.

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]
print(inverso)
print(junto)

if inverso == junto:
    print('É um palindromo')

else:
    print('Não é um palindromo')

