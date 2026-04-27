'''Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

n = int(input('Digite um número inteiro: '))

a = n - 1
s = n + 1 

print('Analisando o número {}, seu sucessor é {} e seu antecessor é {}.'.format(n, s, a))

'''ou pode ser feito da seguinte forma:

n = int(input('Digite um número inteiro: '))
print('Analisando o número {}, seu sucessor é {} e seu antecessor é {}.'.format(n, (n + 1), (n - 1)))

'''