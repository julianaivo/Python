'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

#obs: as funções trigonométricas devem estar em radianos. Para isso utilizamos o math.radians(x)

import math
angulo = float(input('Digite o ângulo que você deseja: '))

s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))

print('O ângulo de {} graus tem o SENO de {:.2f}'.format(angulo, s))
print('O ângulo de {} graus tem o COSSENO de {:.2f}'.format(angulo, c))
print('O ângulo de {} graus tem a TANGENTE de {:.2f}'.format(angulo, t))