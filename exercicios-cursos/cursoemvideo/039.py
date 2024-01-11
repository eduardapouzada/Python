# Leia o ano de nascimento, e informe se ainda vai se alistar, se é a hora exata de se alistar ou se já passou do tempo de se alistar. Também deve mstrar o tempo que falta ou que passou do prazo.

ano = int(input('Ano de nascimento: '))

if ano == 2005:
    print('Quem nasceu em 2005, tem 18 anos. \nVocê tem que se alistar imediatamente.')
    
elif ano < 2005:
    print('Quem nasceu em {}, tem {} anos. \nVocê já deveria ter se alistado há {} anos. \nSeu alistamento foi em {}.' .format(ano, 2023 - ano,  2023 - (ano + 18) , ano + 18))
    
elif ano > 2005:
    print('Quem nasceu em {}, tem {} anos. \nAinda faltam {} anos para seu alistamento. \nSeu alistamento será em {}.' .format(ano, 2023 - ano, (ano + 18) - 2023,  ano + 18))
    
else:
    print('Ano inválido.')    