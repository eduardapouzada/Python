nome = str(input('Qual seu nome completo: ')).strip()

nome = nome.split()

print('Prazer em te conhecer!')
print('Seu primeiro nome é {}.' .format(nome[0]))
print('Seu ultimo nome é {}.' .format(nome[len(nome)-1]))
