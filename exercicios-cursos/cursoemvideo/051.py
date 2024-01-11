# PA

p1 = int(input('Digite o primeiro termo: '))
razão = int (input('Digite a razão: '))
decimo = p1 + (10-1) *razão
for a in range (p1, decimo + razão, razão):
    print(a, end=' - ')