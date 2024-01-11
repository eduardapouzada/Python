from random import shuffle

um = str(input('Pirmeiro aluno:'))
dois = str(input('Segundo aluno: '))
tres = str(input('Terceiro aluno: '))
quatro = str(input('Quarto aluno: '))

lista = [um, dois, tres, quatro]

shuffle(lista)

print('A ordem de apresentação sera: {}' .format(lista))


# Leia o nome de quatro alunos e mostre a ordem sorteada para a apresentação dos trabalhos.