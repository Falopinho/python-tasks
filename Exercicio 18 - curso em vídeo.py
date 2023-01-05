from math import cos, tan, sin, radians
angulo = float(input('Digite o Ângulo: '))
seno = sin(radians(angulo))
print('O Ângulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O Ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O Ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, tangente))