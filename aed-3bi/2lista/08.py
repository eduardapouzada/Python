"""   
Faça um programa, em Python, que manipule um arquivo conforme segue:
a) Cria um arquivo alunos.txt, e insira os dados de pelo menos três alunos
informados pelo usuário, sendo o nome, o número de matrícula e suas notas nos primeiros
três bimestres do ano (veja quadro). Atenção para a organização dos dados e o delimitador
empregado;

João=2345=8.5=6.4=9.2
Maria=1234=10.0=5.0=3.5
Marcos=4567=5.0=8.0=9.5

b) Após, abra o arquivo alunos.txt criado e mostre o conteúdo de cada linha. Em
seguida, informe a média de cada aluno, e se ele foi aprovado ou reprovado. Considere que
para a aprovação a média deve ser igual ou maior a 7.0.

"""
with open('aed-3bi/2lista/alunos.txt', 'r+', encoding='utf-8') as arquivoAlunos: 

    for i in range(1,3 + 1):
        nome = str(input(f'Informe o nome do {i} aluno: '))
        arquivoAlunos.write(nome + '=')
        for a in range(1):
            matricula = int(input(f'Informe o número da matricula do aluno:'))
            arquivoAlunos.write(str(matricula) + '=')
            for b in range(1,3+1):
                nota = float(input(f'Informe a nota do bimestre {b}: '))
                
                if b == 3:
                    arquivoAlunos.write(str(nota) + '\n')
                    
                else:    
                    arquivoAlunos.write(str(nota) + '=')
                
            
        