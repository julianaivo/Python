'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc

valor = float(input('Digite um valor: '))

valor_inteiro = trunc(valor)

print('O valor digitado foi {} e sua porção inteira é {}.'.format(valor, valor_inteiro))

'''
Nesse caso optei por importar apenas UMA funcionalidade e, por essa razão, não foi necessário o uso do math. já que o Python traz o método direto para a pasta. Esse exercício também poderia ser realizado da seguinte maneira:

import math

valor = float(input('Digite um valor: '))

print('O valor digitado foi {} e sua porção inteira é {}.'. format(valor, math.trunc(valor)))

Outra forma de fazer sem precisar utilizar a biblioteca math seria:

valor = float(input('Digite um valor: '))

print('O valor digitado foi {} e sua porção inteira é {}.'.format(valor, int(valor)))
'''