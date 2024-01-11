# ler o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Qual é o primeiro termo? '))
razão = int(input('E qual a razão? '))
termos = 2

resul = primeiro + razão
print(primeiro, '➙', end=' ')
while termos != 11:
    termos += 1
    print(f'{resul} ➙', end=' ')
    resul = resul + razão
print('FIM')
