'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

#não é obrigatório por o str() mas, é uma forma de deixar explícito que irá ler uma string.

import random 

n1 = input('Primeiro aluno: ')
n2 = input('Segunod aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

print('O aluno escolhido foi', random.choice(lista))




'''
Ou poderia por uma variável para o item random, exemplo:

import random 

n1 = input('Primeiro aluno: ')
n2 = input('Segunod aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}',format(escolhido))
'''