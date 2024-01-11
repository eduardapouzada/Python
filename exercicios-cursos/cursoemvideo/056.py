#  leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
#  qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
idade_homem = 0
velho = ''
total_mulheres = 0

for pessoas in range(1, 5):
    print(f'--- {pessoas}ª PESSOA ---')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F, M]: ')).upper()

    soma = soma + idade
    media = soma / 4

    if pessoas == 1 and sexo == 'M':
        idade_homem = idade
        velho = nome

    if sexo == 'M' and idade_homem < idade:
        idade_homem = idade
        velho = nome

    if sexo == 'F' and idade < 20:
        total_mulheres += 1


print(f'A media da idade do grupo é: {media}')
print(f'O homem mais velho se chama {velho} e tem {idade_homem} anos.')
print(f'O total de mulheres menores de 20 anos é {total_mulheres}')