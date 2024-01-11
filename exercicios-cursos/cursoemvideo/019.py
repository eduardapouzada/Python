from random import choice

um = str(input('Pirmeiro aluno:'))
dois = str(input('Segundo aluno: '))
tres = str(input('Terceiro aluno: '))
quatro = str(input('Quarto aluno: '))

lista = [um, dois, tres, quatro]
escolhido = choice(lista)

print('O aluno escolhido foi: {}' .format(escolhido))

# Leia nomes e escolhe um.