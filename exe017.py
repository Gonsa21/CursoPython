import math
co = float(input('Digite o valor do cateter oposto: '))
ca = float(input('Digite o valor do cateter adjacente: '))
rco = math.pow(co, 2)
rca = math.pow(ca, 2)
result = math.sqrt(rco + rca)
print('O valor da hipotenusa é {:.2f}.'.format(result))
