# Tabuada com laço for

tab = int(input('Qual tabuada? '))
a = 0
for t in range (0 , 10):
    a = a + 1
    r = tab * a
    print('{} x {} = {}' .format(a, tab, r))