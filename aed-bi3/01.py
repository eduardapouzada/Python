""" 
 Imagine que você está conduzindo um experimento científico em um
laboratório e deseja analisar os dados coletados. Os dados são representados em
forma de listas em um arquivo texto, e você precisa criar um programa em Python
para realizar algumas operações de análise de dados.
O arquivo possui o seguinte formato:
● 1ª linha: uma lista de temperaturas medidas em graus Celsius, separadas por
vírgula.
● 2ª linha: uma lista de pressões medidas em Pascal, separadas por vírgula.
● 3ª linha: uma lista de nomes dos experimentos correspondentes, separados
por vírgula.
O programa deve ser capaz de ler esse arquivo e fazer o seguinte:
● Calcular a temperatura média e a pressão média a partir das listas.
● Identificar qual experimento teve a maior temperatura máxima.
● Identificar qual experimento teve a menor pressão mínima.
● Exibir todos os experimentos em que a temperatura seja superior a 25 graus
Celsius.
"""


with open('aed-bi3/arquivo.txt', 'r', encoding='utf-8') as arquivo:
    leitura = arquivo.readlines()
    
    soma = 0 
    for dados in leitura[0].strip().split(','): #! PEGANDO A MEDIA DA TEMPERATURA
        soma += float(dados)
    soma = soma // 5    
        
    print(f'A temperatura média é {soma}') 
    
    soma = 0
    for dados in leitura[1].strip().split(','):
        soma += float(dados) 
    soma = soma // 5    
    print(f'A pressão média é: {soma}')


