"""
Uma empresa de transporte oferece diferentes tarifas com base na
distância percorrida em quilômetros e no tipo de veículo utilizado. Implemente um
programa em Python que solicite ao usuário a distância da viagem e o tipo de
veículo, e calcule o valor total a ser pago. As informações sobre as tarifas estão
descritas a seguir:
Ônibus: R$ 0,50 por Km; Carro: R$ 0,75 por Km; Moto: R$ 0,45
por Km. Além disso, a empresa oferece os seguintes descontos, dependendo da
distância:
Até 100 km: nenhum desconto.
De 101 km a 300 km: 10% de desconto.
Acima de 300 km: 20% de desconto.

Exemplo:
Digite a distância da viagem (em km): 250
Digite o tipo de veículo (ônibus, carro ou moto): carro
Valor total a ser pago: R$ 168,75


"""

disc = float(input('Digite a distância da viagem (em km): '))
veic = str(input('Digite o tipo de veículo (ônibus, carro ou moto): '))

def total(distancia, veiculo):
    if veiculo == 'onibus':
        if distancia > 100 and distancia <= 300:
            preço = 0.50 * distancia
            desconto = preço - (preço * 0.10)
            print(f'Valor total a ser pago: R${desconto}')
    
        elif distancia > 300:
            preço = 0.50 * distancia
            desconto = preço - (preço * 0.20)
            print(f'O valor total a ser pago: R${desconto}')
            
        else:
            preço = 0.50 * distancia
            print(f'O valor total a ser pago: R${preço}')    
    
    
    elif veiculo == 'moto':
        if distancia > 100 and distancia <= 300:
            preço = 0.45 * distancia
            desconto = preço - (preço * 0.10)
            print(f'Valor total a ser pago: R${desconto}')
    
        elif distancia > 300:
            preço = 0.45 * distancia
            desconto = preço - (preço * 0.20)
            print(f'O valor total a ser pago: R${desconto}')
            
        else:
            preço = 0.45 * distancia
            print(f'O valor total a ser pago: R${preço}')  
            
            
    elif veiculo == 'carro':
        if distancia > 100 and distancia <= 300:
            preço = 0.75 * distancia
            desconto = preço - (preço * 0.10)
            print(f'Valor total a ser pago: R${desconto}')
    
        elif distancia > 300:
            preço = 0.75 * distancia
            desconto = preço - (preço * 0.20)
            print(f'O valor total a ser pago: R${desconto}')
            
        else:
            preço = 0.75 * distancia
            print(f'O valor total a ser pago: R${preço}')  
            
    else:
        print(f'{veiculo} inválido.')         
            
                  
total(disc, veic)

