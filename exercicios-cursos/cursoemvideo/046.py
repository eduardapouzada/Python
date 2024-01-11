# Contagem regressiva de 10 a 0 com pausa de 1 segundo.

from time import sleep

for a in range (10, -1, -1):
    sleep(1)
    print(a)
    
print('BUM!')    