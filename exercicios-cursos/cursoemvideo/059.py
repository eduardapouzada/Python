# programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior  [ 4 ] novos números [ 5 ] sair do programa

um = int(input('Primeiro valor: '))
dois = int(input('Segundo valor: '))

opção = 0

while opção != 5:
    opção = int(input('[ 1 ] Somar\n'
                      '[ 2 ] Multiplicar\n'
                      '[ 3 ] Maior\n'
                      '[ 4 ] Menor\n'
                      '[ 5 ] Sair do programa\n'
                      'Qual sua opção? '))

    if opção == 1:
        soma = um + dois
        print(f'A soma dos valores é: {soma}')

    if opção == 2:
        mult = um * dois
        print(f'A multiplicação dos valores é {mult}')

    if opção == 3:
        if um > dois:
            print(f'O maior valor é o {um}')
        else:
            print(f'O maior valor é o {dois}')

    if opção == 4:
        if um < dois:
            print(f'O menor valor é o {um}')
        else:
            print(f'O menor valor é o {dois}')


print('Você saiu do programa!')
