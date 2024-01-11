#  leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [F/M]: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [F/M]: ')).upper()

print(f'Sexo {sexo} registrado com sucesso!')