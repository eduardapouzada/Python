import math 

a = float(input('Qual o angulo?'))

cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
seno = math.sin(math.radians(a))

print('Angulo: {}\n Cosseno: {:.2f}\n Tangente: {:.2f}\n Seno: {:.2f}' .format(a, cos, tan, seno))