'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''

nome = input('Qual seu nome? ')

print('É um prazer te conhecer, ', nome)

'''
# ou poderia ser escrito assim, usando f-string:
print('É um prazer te conhecer, {}!' .format(nome))

#ou ainda:
print(f'É um prazer te conhecer, {nome}!')
'''