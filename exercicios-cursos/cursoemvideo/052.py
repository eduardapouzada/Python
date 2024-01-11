# Primo
num = int(input('Digite um número: '))
qunt = 0
for n in range(1, num + 1):
    if num % n == 0:
        print(f'{n}', end=' ')
        qunt = qunt + 1

if qunt > 2:
        print(f'\nFoi divisivel {qunt} vezes. Então não é primo.')

else:
        print(f'\nFoi divisivel {qunt} vezes. Então é primo')