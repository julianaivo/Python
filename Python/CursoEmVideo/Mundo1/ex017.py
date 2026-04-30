'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

r'''
Representação: 

            |\
            | \
  cateto    |  \   Hipotenusa
  oposto    |   \
            |____\
            
            cateto
            adjacente

obs: o "r" no início serve para usar string “raw”. O "r" diz ao Python: “não interprete escapes”. Dessa forma, evita que o Python interprete a barra invertida \ dentro da string como início de uma sequência de escape (tipo \n, \t, etc.).
'''

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

h = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(h))


'''
Outra forma de fazer, sem o uso da biblioteca math:

co = float(input('Comprimeto do cateto oposto: '))

ca = float(input('Comprimento do cateto adjacente: '))

h = ((co ** 2) + (ca ** 2)) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(h))
'''
