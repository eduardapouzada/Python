""" 
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = ('Flamengo', 'Palmeiras', 'São Paulo', 
         'Atletico', 'Corinthians', 'Fluminense', 'Grêmio', 'Fortaleza', 'Chapecoense', 'Internacional', 'Santos', 
         'Bahia', 'Botafogo', 'Bragantino', 'Atletico-GO', 
         'Ceará', 'América', 'Goiás')

print('==' * 25)
print(f'A lista de time: {times}')
print('==' * 25)
print(f'Os 5 primeiros colocados: {times[:5]}')
print('==' * 25)
print(f'Os ultimos colocados: {times[-4:]}')
print('==' * 25)
print(f'Times em ordem alfabética: {sorted(times)}')
print('==' * 25)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição.')
print('==' * 25)
