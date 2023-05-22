import math
'''ang = int(input('Digite aqui o Ângulo: '))
rad = math.radians(ang)
se = math.sin(rad)
co = math.cos(rad)
ta = math.tan(rad)
print('Dado o ângulo o seu seno é {:.2f}, e seu cosseno é {:.2f} e tangente é {:.2f}.'.format(se, co, ta))'''

an = float(input('Digite um angulo: '))
se = math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}.'.format(an,se))
co = math.cos(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}.'.format(an,co))
tg = math.tan(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}.'.format(an,tg))
